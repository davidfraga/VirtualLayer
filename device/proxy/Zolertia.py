'''
Created on 27/09/2013

@author: david
'''
from datetime import datetime
import os
import sys
import threading
import time
import usb


UPDATING = 0
RUNNING = 0

INTERFACE = 0
ENDPOINT = 1
SIZE = 20

OS_WINDOWS = "win32"
OS_LINUX = "linux2"
WINDOWS_EXEC = "tools/serialdump-windows.exe"
LINUX_EXEC = "tools/serialdump-linux"
LINUX_SERIAL_PORTS = "/dev/ttyUSB*"
WINDOWS_SERIAL_PORTS = "MODE.COM"

class Zolertia(threading.Thread):
    '''
    Proxy for the Zolertia Hardware connected to USB
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self._device = None
        self._sensors = []
        self._handle = None
        self._port = ""
        self._os = sys.platform
        self._close = False
        self._data = tuple()
        self._status = RUNNING
    
    def __del__(self):
        self._handle.releaseInterface()
        self._device.attach_kernel_driver(INTERFACE)        
    
    def setDevice(self,device):        
        self._device = device
        '''
        intf = self._device._ctx
        print("INTERFACE: "+str(intf))
        legacyDevice = usb.legacy.Device(device)
        self._handle = legacyDevice.open()
        '''
        if self._os == OS_LINUX:
            p = os.popen("ls "+LINUX_SERIAL_PORTS,"r")
            ports = []
            while True:
                line = p.readline()
                if not line:
                    break
                
                ports.append(line[:-1])
            if len(ports)==1:
                self._port = ports[0]
               
            print("PORTAS: "+str(ports))
        
        
    def detachingDevice(self):
        if self._device.is_kernel_driver_active(INTERFACE):
            print("KERNEL DRIVER ACTIVE")
            self._device.detach_kernel_driver(INTERFACE)
    
    def write(self, msg):
        pass
    
    def run(self):        
        p = os.popen("./"+LINUX_EXEC+" -b115200 "+self._port,"r")
        while not self._close:
            line = p.readline()
            if not line:
                pass
            else:
                self._status = UPDATING
                # TODO: format data
                self._data = (datetime.now(), line[:-1])
                self._status = RUNNING
    
    def read(self):
        '''
        p = os.popen("./"+LINUX_EXEC+" -b115200 "+self._port,"r")
        line = p.readline()
        if not line:
            return None
        else:
            return line[:-1]
        '''
        return self._data 
'''
Created on 27/09/2013

@author: david
'''
import pkgutil

from device.proxy import Zolertia
from main import Discovery

PROXY_MODULE_PATH = 'device/proxy'
PROXY_PACKAGE_NAME = 'device.proxy'

class DeviceManager(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self._proxies = [name for _, name, _ in pkgutil.iter_modules([PROXY_MODULE_PATH])]
        self._activeDevices = {}
        self._discovery = Discovery.FindUSB(self.update)
        self._discovery.start()        
    
    def update(self, actionToRemove, data):
        print("action -> "+str(actionToRemove))
        if actionToRemove:
            print("removing "+data)
            del self._activeDevices[data]
        else: 
            for key in data.keys():
                print("Adding "+key)                
                print(self._proxies)                
                if key.capitalize() in self._proxies:                    
                    proxy = self._get_class(key.capitalize())()
                    print(proxy)
                    proxy.setDevice(data[key])
                    proxy.start()                
                    self._activeDevices[key] = proxy
    
    def getActiveDevicesNames(self):
        return self._activeDevices.keys()
    
    def readFromDevice(self, deviceKey):
        if deviceKey in self._activeDevices.keys():
            device = self._activeDevices[deviceKey]
            print("DEVICE: "+str(device))
            data = device.read()
            print("DATA: "+str(data))
            return data
    
    def _get_class( self, className ):
        name = PROXY_PACKAGE_NAME+"."+className+"."+className
        parts = name.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )
        for comp in parts[1:]:
            m = getattr(m, comp)            
        return m
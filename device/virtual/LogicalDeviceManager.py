'''
Created on 27/09/2013

@author: david
'''
from device.DeviceManager import DeviceManager
from device.virtual.LogicalDevice import LogicalDevice

# Logical Devices situation types
REGISTERED = 0
UNREGISTERED = 1

class LogicalDeviceManager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._logicalDevices = []
        self._deviceManager = DeviceManager()
    
    def registerLogicalDevice(self,logicalname,devicesNames):
        print("active devices: "+str(list(self._deviceManager.getActiveDevicesNames())))
        print("device chosen: "+str(devicesNames))      
        if set(devicesNames).issubset(self._deviceManager.getActiveDevicesNames()):
            if self._getLogicalReaderByName(logicalname) == None:
                logicalDevice = LogicalDevice(logicalname,devicesNames)
                self._logicalDevices.append(logicalDevice)
                return REGISTERED
            return "LOGICAL READER EXISTS"
        return "DEVICES NAMES NOT EXISTS"
            
    def unregisterLogicalDevice(self, logicalname):
        logicalDevice = self._getLogicalReaderByName(logicalname)
        if logicalDevice != None:
            self._logicalDevices.remove(logicalDevice)
            return UNREGISTERED
                
    def _getLogicalReaderByName(self, logicalname):
        for logdev in self._logicalDevices:
            if logdev.getLogicalDeviceName() == logicalname:
                return logdev
        return None
    
    def write(self,logicalname,msg):
        # TODO implement method
        pass
    
    def read(self,logicalname):
        logicalDevice = self._getLogicalReaderByName(logicalname)
        if logicalDevice != None:
            data = []
            for deviceName in logicalDevice.getPhysicalsDevicesNames():
                data.append(self._deviceManager.readFromDevice(deviceName))
            
            return data
        return None
'''
Created on 27/09/2013

@author: david
'''

class LogicalDevice(object):
    '''
    classdocs
    '''
    
    

    def __init__(self, name, devicesNames):
        '''
        Constructor
        '''
        self._name = name
        self._devicesNames = devicesNames
    
    def getLogicalDeviceName(self):
        return self._name
    
    def getPhysicalsDevicesNames(self):
        return self._devicesNames
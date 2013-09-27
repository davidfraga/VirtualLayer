'''
Created on 27/09/2013

@author: david
'''
from main import Discovery


class USBDiscovery(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
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
                self._activeDevices[key] = data[key]
    
    def getActiveDevices(self):
        return self._activeDevices
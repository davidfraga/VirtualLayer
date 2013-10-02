'''
Created on 27/09/2013

@author: david
'''

MAX_READINGS = 5

class Sensor(object):
    '''
    classdocs
    '''


    def __init__(self, type):
        '''
        Constructor
        '''
        self._type = type
        self._readings = []
        
    def addReading(self, data):
        if len(self._readings) >= MAX_READINGS:
            self._readings.pop()
            
        self._readings.insert(0, data)
    
    def getReadings(self):
        return self._readings
        

class SensorType(object):
    TEMPERATURE = 1
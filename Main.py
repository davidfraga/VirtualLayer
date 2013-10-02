'''
Created on 27/09/2013

@author: david
'''
import time

from device.virtual.LogicalDeviceManager import LogicalDeviceManager


if __name__ == '__main__':
    logicalName = "primeiro logical device"
    deviceName = ["zolertia"]
    logicaldevicemanager = LogicalDeviceManager()
    time.sleep(3)
    print("SITUATION: "+str(logicaldevicemanager.registerLogicalDevice(logicalName, deviceName)))
    
    while(True):
        print("READ: "+str(logicaldevicemanager.read(logicalName)))
        time.sleep(3)
    
    
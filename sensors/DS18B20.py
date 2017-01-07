#!/usr/bin/python
#Up2Strat project
#

from sensors.SensorInterface import SensorInterface

from os import system
from time import sleep

# Class providing access to DS18B20 Sensor
# Todo :
#   - add func docs
#   - add comments
#   - add logger
class DS18B20(SensorInterface):
    def __init__(self, sensorId, sensorPath):
        self.sensorPath = sensorPath
        self.sensorId = sensorId
        self.sensorDataFilePath = "{0}/{1}/w1_slave".format(self.sensorPath, self.sensorId)
        system('modprobe w1-gpio')
        system('modprobe w1-therm')

    def setWaitInterval(self, intervalMS):
        self.waitInterval = intervalMS

    def setTimeoutInterval(self, intervalMS):
        self.timeoutInterval = intervalMS

    def read(self, wait=False):
        while self.isReady() != True:
            if wait == False:
                # Deal w/ our own Exception, e.g. SensorException
                raise Exception("Sensor#{0} is not ready yet".format(self.sensorId))
            sleep(0.2)
        self.fileHandler = open(self.sensorDataFilePath, 'r')
        lineList = self.fileHandler.readlines()
        self.fileHandler.close()
        rawValue = lineList[1].split("=")[1]
        return round(int(rawValue) / 1000.0, 2)

    def isReady(self):
        self.fileHandler = open(self.sensorDataFilePath, 'r')
        lineList = self.fileHandler.readlines()
        self.fileHandler.close()
        if len(lineList) < 2:
            return False
        return (lineList[0].rstrip('\n')[-3:] == 'YES')

    def __exit__(self, exc_type, exc_value, traceback):
        self.fileHandler.close()

#!/usr/bin/python
#Up2Strat project
#

from sensors.DS18B20 import DS18B20

#Testing a fake file
sensorId = 's1'
sensorDataPath = "./"

s1 = DS18B20(sensorId, sensorDataPath)
if s1.isReady():
    celisiusTemp = s1.read()
    print("t={0}°C".format(celisiusTemp))

# rpi-sensors

Simple classes providing access to sensor.
 * DS18B20 (temperature)

## Use

### DS18B20 (temperature)
DS18B20 stores info in file : `/sys/bus/w1/devices/<sensor identifier>/W1_slave`
e.g. :
```
7c 01 4b 46 7f ff 04 10 09 : crc=09 YES
7c 01 4b 46 7f ff 04 10 09 t=23750
```


```Python
from sensors.DS18B20 import DS18B20
sensorId = '28-00042d8165ff'
sensorDataPath = '/sys/bus/w1/devices/'
s1 = DS18B20(sensorId, sensorDataPath)
if s1.isReady():
    celisiusTemp = s1.read()
    print("t={0}°C".format(celisiusTemp))
```

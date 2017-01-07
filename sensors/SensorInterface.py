#!/usr/bin/python
#Up2Strat project
#

import abc

class SensorInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def setWaitInterval(self, intervalMS = 10000):
        pass

    @abc.abstractmethod
    def setTimeoutInterval(self, intervalMS = 10000):
        pass

    @abc.abstractmethod
    def read():
        pass

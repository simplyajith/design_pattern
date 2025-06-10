from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def registerObserver(self,obj):
        pass

    @abstractmethod
    def removeObserver(self,Obj):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def display(self,v):
        pass

class WeatherStation(Subject):
    temperature = 0

    def __init__(self):
        self.observers = {}

    def registerObserver(self,ObserverObj):
        self.observers[ObserverObj] = 1
        print(self.observers)


    def removeObserver(self,ObserverObj):
        del self.observers[ObserverObj]

    def notifyObservers(self):
        for i in self.observers:
            i.display(self.temperature)

    def settemperature(self,val):
        self.temperature = val
        self.notifyObservers()

class Logger(Observer):

    def __init__(self,weatherstation):
        self.weatherstation = weatherstation
        weatherstation.registerObserver(self)


    def display(self,val):
        print("temperature is ", val)


class Logger2(Observer):

    def __init__(self, weatherstation):
        self.weatherstation = weatherstation
        weatherstation.registerObserver(self)

    def display(self, val):
        print("logger2: temperature is ", val)

    def remove_subscription(self):
        self.weatherstation.removeObserver(self)



weather = WeatherStation()
logger1 =   Logger(weather)
logger2 =   Logger2(weather)
logger3= Logger(weather)
weather.settemperature(50)
logger2.remove_subscription()
weather.settemperature(40)



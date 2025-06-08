from abc import ABC, abstractmethod


class DuckSimulator:

    def __init__(self,duck):
        self.duck = duck

    def test_duck(self):
        self.duck.quack()
        self.duck.fly()


class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass

class MallardDuck(Duck):

    def quack(self):
        print("quack, quack, mallard duck")


    def fly(self):
        print("fly, fly, mallard duck")


mallard  = MallardDuck()
DuckSimulator(mallard).test_duck()


#Challenge need to use following Drone in duck simulator

class Drone(ABC):

    @abstractmethod
    def beep(self):
        pass

    @abstractmethod
    def spin_motors(self):
        pass

class SuperDrone(Drone):

    def beep(self):
        print("SuperDrone, beep,beep")

    def spin_motors(self):
        print("spin,spin, super Drone")


class SuperDroneAdapter(Duck):

    def __init__(self,drone):
        self.drone = drone


    def quack(self):
        self.drone.beep()

    def fly(self):
        self.drone.spin_motors()


super1 = SuperDrone()
super1adapt = SuperDroneAdapter(super1)
DuckSimulator(super1adapt).test_duck()



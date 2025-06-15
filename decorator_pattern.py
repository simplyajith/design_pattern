from abc import abstractmethod, ABC


class Beverage(ABC):

    @abstractmethod
    def getDescription(self):
        pass
    @abstractmethod
    def cost(self):
        pass

class CondimentDecorator(Beverage):

    def getDescription(self):
        pass


class HouseBlend(Beverage):


    def getDescription(self):
        return "Enjoy with HouseBlend "

    def cost(self):
        return 0.99


class DarkRoast(Beverage):


    def getDescription(self):
        return "Enjoy with Darkroast "

    def cost(self):
        return 0.99

class Milk(CondimentDecorator):
    def __init__(self,beverage):
        self.beverage = beverage


    def getDescription(self):

        return self.beverage.getDescription()+ " + Milk"

    def cost(self):
        return self.beverage.cost() + 0.15

class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + " + Mocha"

    def cost(self):
        return self.beverage.cost() + 0.20

class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + " + Whip"

    def cost(self):
        return self.beverage.cost() + 0.10

class Size:
    TALL = "TALL"
    GRANDE = "GRANDE"
    VENTI = "VENTI"


darkroast = DarkRoast()
print(darkroast.getDescription())
print(darkroast.cost())
darkroast = Milk(darkroast)
print(darkroast.getDescription())
print(darkroast.cost())
darkroast = Milk(darkroast)
print(darkroast.getDescription())
print(darkroast.cost())
darkroast = Mocha(darkroast)
print(darkroast.getDescription())
print(darkroast.cost())
darkroast = Whip(darkroast)
print(darkroast.getDescription())
print(darkroast.cost())








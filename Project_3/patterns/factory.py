import abc
from Project_3.gilded_rose import Inventory
from Project_3.patterns.observer import *


class Factory_interface(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def create_empty(self):
        raise NotImplementedError

    @abc.abstractmethod
    def create_filled(self, item):
        raise NotImplementedError


class Inventory_factory(Factory_interface):
    """
    Creates several types of inventories with all 4 seasons instantiated
    """

    def __init__(self, name):
        self.name

    def create_empty(self)
        winter = Winter()
        spring = Spring() 
        summer = Summer()
        fall = Fall()
        seasons = [winter, spring, summer, fall]
        inventory = Inventory(items=None, seasons=seasons)
        return inventory

    def create_filled(self, items)
        winter = Winter()
        spring = Spring() 
        summer = Summer()
        fall = Fall()
        seasons = [winter, spring, summer, fall]
        inventory = Inventory(items=items, seasons=seasons)
        return inventory




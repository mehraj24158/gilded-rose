import abc
from Project_3.gilded_rose import Inventory
from Project_3.patterns.decorator import *
class Gift_basket_factory_interface(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def create(self):
        raise NotImplementedError

class Gift_basket_factory(Gift_basket_factory_interface):

    def __init__(self, name=None):
        self.name = name

    def create(self, items, total_quality):
        items_quality = 0
        for item in items:
            items_quality += item.get_quality()
        
        if items_quality >= total_quality:
            raise AssertionError("Cannot have items with quality greater than desired quality")
            return items
        else:
            gift_basket = Gift_basket_wrapper(items=items, quality = total_quality-items_quality)
            return gift_basket
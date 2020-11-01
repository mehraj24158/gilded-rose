import abc
# from patterns.observer import Observer_interface
from Project_3.patterns.observer import Observer_interface

class Item_interface(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def update():
        raise NotImplementedError

    @abc.abstractmethod
    def get_quality():
        raise NotImplementedError

    @abc.abstractmethod
    def get_sell_in():
        raise NotImplementedError

    @abc.abstractmethod
    def set_quality():
        raise NotImplementedError

    @abc.abstractmethod
    def set_sell_in():
        raise NotImplementedError


class Item(Item_interface, Observer_interface):
    """
    Implementation of item class
    Now stores function behavior in item_type attribute
    """
    def __init__(self, name, sell_in, quality, item_type, degradation_rate = 1,):
        self.name = name
        self._sell_in = sell_in
        self._quality = quality
        self.degradation_rate = degradation_rate
        self.item_type = item_type
        
        self.quality_modifier = 0
        self.sell_in_modifier = 0

    def update(self):
        if self.item_type is None:
            raise Exception(" You must set Item Type!!")

        self._sell_in, self._quality = self.item_type.update(self._sell_in, self._quality, self.degradation_rate)

    def update_season(self, qm, sm):
        self.quality_modifier = qm
        self.sell_in_modifier = sm

    def get_quality(self):
        return self._quality + self.quality_modifier
            
    def get_sell_in(self):
        return self._sell_in + self.sell_in_modifier
    
    def set_quality(self, quality):
        self._quality = quality

    def set_sell_in(self, sell_in):
        self._sell_in = sell_in

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self._sell_in, self._quality)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            for self_attribute, other_attribute in zip(vars(self), vars(other)):
                if getattr(self, self_attribute) != getattr(other, other_attribute):
                    return False
            return True
        else:
            return False

class Inventory_interface(metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def update(self):
        raise NotImplementedError

    @abc.abstractmethod
    def clean(self):
        raise NotImplementedError

    @abc.abstractmethod
    def clean_update(self):
        raise NotImplementedError

class Inventory(Inventory_interface):
    def __init__(self, items=None, seasons=None, cookies = 0):
        self.items = items
        self.seasons = seasons
        self.expired = []
        
    def update(self):
        for item in self.items:
            item.update()

    def clean(self):
        for item in self.items:
            if item.get_sell_in <= 0:
                self.item.remove(item)

    def clean_update(self):
        self.update()
        self.clean()
        
    def print_all(self):
        for item in self.items:
            print(repr(item))

    def __str__(self):
        items = []
        for item in self.items:
            items.append(repr(item))
        
        return str(items)
import abc
class Decorator_interface(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def wrap(self, item):
        raise NotImplementedError

    @abc.abstractmethod
    def unwrap(self, item):
        raise NotImplementedError

class Gem(Decorator_interface):
    def __init__(self, quality, item = None, name = None):
        self.item = item
        self._quality = quality
        self.name = name

    def get_quality(self):
        if self.item is None:
            return self._quality
        else:
            return self._quality + self.item.get_quality()

    def wrap(self, item):
        self.item = item

    def unwrap(self):
        return self.item

class Gift_basket_wrapper(Decorator_interface):
    def __init__(self, quality, items = None, name = None):
        self.items = items
        self._quality = quality
        self.name = name

    def get_quality(self):
        total_quality = 0
        for item in self.items:
            total_quality += item.get_quality()

        return total_quality + self._quality

    def wrap(self, items):
        self.items = items

    def unwrap(self):
        return self.items
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
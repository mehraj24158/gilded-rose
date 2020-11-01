import abc
class item_behavioral_interface(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def bound():
        raise NotImplementedError
    
    @abc.abstractmethod
    def update():
        raise NotImplementedError

class Common(item_behavioral_interface):
    def __init__(self):
        self.type = "Common Item"

    def bound(self, quality):
        if quality > 50:
            quality = 50
        if quality < 0: 
            quality = 0
        return quality

    def update(self, sell_in, quality, degradation_rate):
        sell_in -= 1
        if sell_in <= 0:
            quality -= (2*degradation_rate)
        else:
            quality -= degradation_rate
        quality = self.bound(quality)
        return sell_in, quality

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            for self_attribute, other_attribute in zip(vars(self), vars(other)):
                if getattr(self, self_attribute) != getattr(other, other_attribute):
                    return False
            return True
        else:
            return False

class Conjured(Common):
    def __init__(self):
        self.type = "Conjured Item"

    def update(self, sell_in, quality, degradation_rate):
        sell_in -= 1
        degradation_rate = degradation_rate * 2
        if sell_in <= 0:
            quality -= (2*degradation_rate)
        else:
            quality -= degradation_rate
        quality = self.bound(quality)
        return sell_in, quality

class Legendary(Common):
    def __init__(self):
        self.type = "Legendary Item"

    def update(self, sell_in, quality, degradation_rate):
        return sell_in, 80

class Aged(Common):
    def __init__(self):
        self.type = "Aged Item"

    def update(self, sell_in, quality, degradation_rate):
        sell_in -= 1
        quality += 1
        quality = self.bound(quality)
        return sell_in, quality

class BackStagePass(Common):
    def __init__(self):
        self.type = "Back Stage Pass Item"

    def update(self, sell_in, quality, degradation_rate):
        sell_in -= 1
        if sell_in <= 5:
            quality += 3
        if sell_in <=10 and sell_in > 5:
            quality += 2
        if sell_in > 10:
            quality += 1
        if sell_in <= 0:
            quality = 0
        quality = self.bound(quality)
        return sell_in, quality
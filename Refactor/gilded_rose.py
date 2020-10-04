class Item:
    """
    Implementation of generic item class
    """
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.degradation_rate = 1

    def bounds(self):
        if self.quality > 50:
            self.quality = 50
        if self.quality < 0 or self.sell_in < 0:
            self.quality = 0

    def update(self):
        self.sell_in -= 1

        if self.sell_in <= 0:
            self.quality -= (2*self.degradation_rate)
        else:
            self.quality -= self.degradation_rate

        self.bounds()

    def getQuality(self):
        return self.quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.getQuality())

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            for self_attribute, other_attribute in zip(vars(self), vars(other)):
                if getattr(self, self_attribute) != getattr(other, other_attribute):
                    return False
            return True
        else:
            return False

class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        super(ConjuredItem, self).__init__(name, sell_in, quality)
        self.degradation_rate = 2
    
class LegendaryItem(Item):
    def __init__(self, name, sell_in=None, quality=None):
        super(LegendaryItem, self).__init__(name, sell_in=None, quality=80)
        self.degradation_rate = 0

    def update(self):
        pass
    
    def bounds(self):
        pass

class Aged(Item):
    def __init__(self, name, sell_in, quality):
        super(Aged, self).__init__(name, sell_in, quality)
    
    def update():
        self.sell_in -= 1
        self.quality += 1
        self.bounds()

class BackStagePass(Item):
    def __init__(self, name, sell_in, quality):
        super(BackStagePass, self).__init__(name, sell_in, quality)

    def update(self):
        self.sell_in -= 1

        if self.sell_in <= 5:
            self.quality += 3
        if self.sell_in <=10 and self.sell_in > 5:
            self.quality += 2
        if self.sell_in > 10:
            self.quality += 1

        self.bounds()
        self.modify()


class Inventory():
    def __init__(self, items):
        self.items = items
        
    def update(self):
        for item in self.items:
            item.update()
        
    def print_all(self):
        for item in self.items:
            print(repr(item))

    def __str__(self):

        items = []
        for item in self.items:
            items.append(repr(item))
        
        return str(items)





# class BackStagePass(Item):
#     def __init__(self, name, sell_in, quality):
#         super(BackStagePass, self).__init__(name, sell_in, quality)
#         self.modifier = 0
#         self.modify()
#         self.quality = quality
#         #self.total = quality + modifier

#     def modify(self):
#         if self.sell_in <= 10 and self.sell_in > 5:
#             self.modifier = 2
#         if self.sell_in <= 5:
#             self.modifier = 3
#         if self.sell_in <= 0:
#             self.modifier = 0

#     def update(self):
#         self.sell_in -= 1
#         self.bounds()
#         self.modify()

#     def getQuality(self):
#         if self.quality + self.modifier >= 50:
#             return 50
#         else:
#             return self.quality + self.modifier
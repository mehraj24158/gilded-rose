class Item:
    """
    Implementation of generic item class
    """
    def __init__(self, name = None, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.expired = False
        self.degradation_rate = 1

    def bounds(self):
        if self.quality > 50:
            self.quality = 50
        if self.quality < 0 or self.sell_in <=0:
            self.quality = 0

    def update(self):
        self.sell_in -= 1

        if sell_in <= 0:
            self.expired = True

        if expired:
            self.quality -= (2*self.degradation_rate)
        else:
            self.quality -= self.degradation_rate

        self.bounds()

    def getQuality(self):
        return self.quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        super(ConjuredItem, self).__init__(name, sell_in, quality)
        self.degradation_rate = 2
    

class LegendaryItem(Item):
    def __init__(self, name, sell_in=None, quality=None):
        super(LegendaryItem, self).__init__(name, sell_in, quality):
        self.sell_in = None
        self.quality = 80
        self.degradation_rate = 0

    def update():
        pass
    
    def bounds():
        pass

class BackStagePass(Item):
    def __init__(self, name=None, sell_in, quality):
        super(Item, self).__init__(self, name = None, sell_in, quality):
        self.modifed = False
        self.modifier = 0

    def modify(self):
        if self.sell_in <= 10 and self.sell_in > 5:
            self.modifier = 2
        if self.sell_in <= 5:
            self.modifier = 3

    def update():
        self.sell_in -= 1

        if sell_in <= 0:
            self.expired = True

        if expired:
            self.quality -= (2*self.degradation_rate)
        else:
            self.quality -= self.degradation_rate

        self.bounds()
        self.modify()

    def getQuality(self):
        return quality + modifier


class Inventory():
    def __init__(self, items):
        self.items = items
        
    def update_inventory(self):
        for item in self.items:
            item.update()

    def print_inventory(self):
        for item in self.items:
            return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    



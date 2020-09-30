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

    def update(self):
        self.sell_in -= self.degradation_rate

        if sell_in <= 0:
            self.expired = True

        if expired:
            self.quality -= (2*self.degradation_rate)
        else:
            self.quality -= self.degradation_rate

        self.bounds()

    def bounds(self):
        if self.quality > 50:
            self.quality = 50
        if self.quality < 0:
            self.quality = 0

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ConjuredItem(Item):
    def __init__():
        super(Item, self).__init__(self, name = None, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.expired = False
        self.degradation_rate = 2
    

class LegendaryItem(Item):
    def __init__():
        super(Item, self).__init__(self, name = None, sell_in, quality):
        self.name = name
        self.sell_in = None
        self.quality = 80
        self.expired = False
        self.degradation_rate = 0

    def update():
        pass
    
    def bounds():
        pass

class BackStagePass(Item):
    def __init__():
        super(Item, self).__init__(self, name = None, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.expired = False
        self.degradation_rate = 1

    def update():
        


    

class Inventory():
    def __init__(self, items):
        self.items = items
        
    def update_inventory(self):
        for item in self.items:
            item.update()

    def print_inventory(self):
        for item in self.items:
            return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    



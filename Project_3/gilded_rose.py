class Item():
    """
    Implementation of item class
    Now stores function behavior in item_type attribute
    """
    def __init__(self, name, sell_in, quality, item_type, degradation_rate = 1, item = None):
        self.name = name
        self._sell_in = sell_in
        self._quality = quality
        self.degradation_rate = degradation_rate
        self.item_type = item_type
        
        self.quality_modifier = 0
        self.sell_in_modifier = 0

        self._item = item

    def update(self):
        if self.item_type is None:
            raise Exception(" You must set Item Type!!")

        self._sell_in, self._quality = self.item_type.update(self._sell_in, self._quality, self.degradation_rate)

    def update_season(self, qm, sm):
        self.quality_modifier = qm
        self.sell_in_modifier = sm

    def get_quality(self):
        if self._item is None:
            return self._quality + self.quality_modifier
        else:
            return self._quality + self.quality_modifier + self._item.get_quality()
            
    def get_sell_in(self):
        return self._sell_in + self.sell_in_modifier
    
    def set_quality(self, quality):
        self._quality = quality

    def set_sell_in(self, sell_in):
        self._sell_in = sell_in
    
    def wrap(self, item):
        self._item = item
    
    def unwrap(self):
        self._item = None


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


def factory():
    def __init__(self):
        pass

    def create_default(self):
        """
        Create Inventory with season objects ready
        """


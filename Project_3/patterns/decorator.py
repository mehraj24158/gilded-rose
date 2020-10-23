class Gem():
    def __init__(self, quality, item = None):
        self.item = item
        self.quality = quality

    def get_quality(self):

        if self.item is None:
            return self.quality
        else:
            return self.quality + self.item.get_quality()
from gilded_rose import *
from datetime import datetime
from patterns.observer import *
from patterns.strategy import *
from patterns.decorator import *
from patterns.adapter import *

items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20, item_type=Common()),
        Item(name="Aged Brie", sell_in=2, quality=0, item_type=Aged()),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7, item_type=Common()),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80, item_type=Legendary()),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80, item_type=Legendary()),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20, item_type=BackStagePass()),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=27, item_type=BackStagePass()),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=42, item_type=BackStagePass()),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=49, item_type=BackStagePass()),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6, item_type=Conjured()),  
        ]

# inventory = Inventory(items)

a = Item(name="+5 Dexterity Vest", sell_in=10, quality=20, item_type=Common())

french = French_adapter()

french.adapt(a)

german = German_adapter()

german.adapt(a)
print(french.translate())

print(german.translate())
from gilded_rose import *

items = [
                Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
                BackStagePass(name="Aged Brie", sell_in=2, quality=0),
                Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
                LegendaryItem(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                LegendaryItem(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                BackStagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
                BackStagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
                BackStagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
                ConjuredItem(name="Conjured Mana Cake", sell_in=3, quality=6),  
            ]

inventory = Inventory(items)

inventory.print_all()

print("Hello world")
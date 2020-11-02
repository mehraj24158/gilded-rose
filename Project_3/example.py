from patterns.command import *
from patterns.strategy import *
from gilded_rose import *

items = [
        Item(name="+5 Dexterity Vest", sell_in=9, quality=19, item_type=Common()),
        Item(name="Aged Brie", sell_in=1, quality=1, item_type=Aged()),
        Item(name="Elixir of the Mongoose", sell_in=4, quality=6, item_type=Common()),
    ]

inventory = Inventory(items=items)
clean_command = Clean(inventory=inventory)

WallE = Robot(name="WallE", command=clean_command)
WallE.execute()
assert items == inventory.items

print(inventory.items)

inventory.update()
WallE.execute()
print(inventory.items)

WallE.undo()
print(inventory.items)
#assert Item(name="Aged Brie", sell_in=1, quality=1, item_type=Aged()) not in inventory.items
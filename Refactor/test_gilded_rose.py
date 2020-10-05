import pytest
from Refactor.gilded_rose import *

"""
Global item list for testing. 
"""
items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Aged(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        LegendaryItem(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        LegendaryItem(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        BackStagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        BackStagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=27),
        BackStagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=42),
        BackStagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=49),
        ConjuredItem(name="Conjured Mana Cake", sell_in=3, quality=6),  
        ]

@pytest.fixture
def test_load():
    print("\n----SETUP----")
    gild_rose = Inventory(items)
    print(gild_rose)
    return gild_rose

def test_equality(test_load):
# Ensures the __eq__ method correctly compares items 
    for inventory_item, item in zip(test_load.items, items):
        assert inventory_item == item
    
def test_print(test_load):
# Ensures the Inventory __str__ method correctly prints all items within the inventory
    
    assert str(test_load) == str(['+5 Dexterity Vest, 10, 20', 'Aged Brie, 2, 0', 'Elixir of the Mongoose, 5, 7', 
    'Sulfuras, Hand of Ragnaros, 0, 80', 'Sulfuras, Hand of Ragnaros, -1, 80', 'Backstage passes to a TAFKAL80ETC concert, 15, 20',
     'Backstage passes to a TAFKAL80ETC concert, 10, 27', 'Backstage passes to a TAFKAL80ETC concert, 5, 42', 
     'Backstage passes to a TAFKAL80ETC concert, 2, 49', 'Conjured Mana Cake, 3, 6'])

def test_update(test_load):
# Ensures the update method updates the inventory correctly
    test_load.update()
    new_items = [
        Item(name="+5 Dexterity Vest", sell_in=9, quality=19),
        Aged(name="Aged Brie", sell_in=1, quality=1),
        Item(name="Elixir of the Mongoose", sell_in=4, quality=6),
        LegendaryItem(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        LegendaryItem(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        BackStagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=14, quality=21),
        BackStagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=29),
        BackStagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=45),
        BackStagePass(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=50),
        ConjuredItem(name="Conjured Mana Cake", sell_in=2, quality=4),  
        ]
    assert test_load.items == new_items
import pytest
from Refactor.gilded_rose import *


"""
Global item list for testing. 
"""

items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        BackStagePass(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        LegendaryItem(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        BackStagePass(name="Backstage pass 1", sell_in=15, quality=20),
        BackStagePass(name="Backstage pass 2", sell_in=10, quality=27),
        BackStagePass(name="Backstage pass 3", sell_in=5, quality=42),
        BackStagePass(name="Backstage pass 4", sell_in=2, quality=49),
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
    assert str(test_load) == str(['+5 Dexterity Vest, 10, 20', 'Aged Brie, 2, 3', 'Elixir of the Mongoose, 5, 7', 'Sulfuras, Hand of Ragnaros, None, 80', 'Backstage pass 1, 15, 20', 'Backstage pass 2, 10, 29', 
'Backstage pass 3, 5, 45', 'Backstage pass 4, 2, 50', 'Conjured Mana Cake, 3, 6'])

def test_update(test_load):
# Ensures the update method updates the inventory correctly
# Strings were utilized to easily access the getQuality method alongside other attributes
# Essentially, Strings were easier to implement for the BackStageClass
    test_load.update()
    
    #print(test_load)
    assert str(test_load) == str(['+5 Dexterity Vest, 9, 19', 'Aged Brie, 1, 3', 'Elixir of the Mongoose, 4, 6',
                            'Sulfuras, Hand of Ragnaros, None, 80', 'Backstage pass 1, 14, 20', 'Backstage pass 2, 9, 29',
                            'Backstage pass 3, 4, 45', 'Backstage pass 4, 1, 50', 'Conjured Mana Cake, 2, 4'])

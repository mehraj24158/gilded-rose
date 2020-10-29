import pytest

from Project_3.gilded_rose import *
from Project_3.patterns.strategy import *
from Project_3.patterns.observer import *
from Project_3.patterns.decorator import *
from Project_3.patterns.adapter import *

"""
Global item list for testing. 
"""

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

@pytest.fixture
def test_load():
    print("\n----SETUP----")
    gild_rose = Inventory(items)
    print(gild_rose)
    return gild_rose

def test_equality():
# Ensures the __eq__ method correctly compares items 
    a = Item(name="+5 Dexterity Vest", sell_in=10, quality=20, item_type=Common())
    b = Item(name="+5 Dexterity Vest", sell_in=10, quality=20, item_type=Common())
    assert a == b

    a = Item(name="+5 Dexterity Vest", sell_in=10, quality=20, item_type=Common())
    b = Item(name="+5 Dexterity Vest", sell_in=10, quality=20, item_type=Aged())
    assert a != b

    a = Item(name="+5 Dexterity Vest", sell_in=10, quality=20, item_type=Common())
    b = Item(name="+5 Dexterity Vest", sell_in=5, quality=20, item_type=Common())
    assert a != b

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
        Item(name="+5 Dexterity Vest", sell_in=9, quality=19, item_type=Common()),
        Item(name="Aged Brie", sell_in=1, quality=1, item_type=Aged()),
        Item(name="Elixir of the Mongoose", sell_in=4, quality=6, item_type=Common()),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80, item_type=Legendary()),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80, item_type=Legendary()),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=14, quality=21, item_type=BackStagePass()),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=29, item_type=BackStagePass()),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=45, item_type=BackStagePass()),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=50, item_type=BackStagePass()),
        Item(name="Conjured Mana Cake", sell_in=2, quality=4, item_type=Conjured()),  
        ]
        
    assert test_load.items == new_items

def test_change():
    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20, item_type=Common())
    item.update()
    assert item.get_quality() ==19 and item.get_sell_in() == 9

    item.item_type = Legendary()
    item.update()
    assert item.get_quality() == 80 and item.get_sell_in() == 9

    item.item_type = Conjured()
    item.update()
    assert item.get_quality() == 50 and item.get_sell_in() == 8

    item.update()
    item.update()
    assert item.get_quality() == 46 and item.get_sell_in() == 6

def test_seasons():
    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20, item_type=Common())
    fall = Fall()
    fall.register(item)
    fall.notify()
    item.update()
    assert item.get_quality() == 24 and item.get_sell_in() == 12
    fall.unregister(item)
    fall.notify()
    assert item.get_quality() == 19 and item.get_sell_in() == 9

def test_decorator():
    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20, item_type=Common())
    emerald = Gem(quality=4, item=item)
    assert emerald.get_quality() == 24
    ruby = Gem(quality=7)
    assert ruby.get_quality() == 7
    ruby.wrap(item)
    assert ruby.get_quality() == 27
    item.update()
    assert ruby.get_quality() == 26
    unwrapped = ruby.unwrap()
    assert unwrapped.get_quality() == 19

def test_adapter():
    french_item_adapter = French_adapter()
    charles = French_client()
    charles.le_set_article(french_item_adapter)

    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20, item_type=Common())
    french_item_adapter.adapt(item)
    assert charles.avoir_nom() == "Gilet de Dextérité +5"
    assert charles.avoir_vendre_dans() == 10
    assert charles.avoir_qualite() == 20

    item2 = Item(name="Sulfuras, Hand of Ragnaros", sell_in=15, quality=35, item_type=Common())
    french_item_adapter.adapt(item2)
    assert charles.avoir_nom() == "Sulfuras, Main de Ragnaros"
    assert charles.avoir_vendre_dans() == 15
    assert charles.avoir_qualite() == 35



import pytest
from Project_3.gilded_rose import *
from Project_3.patterns.strategy import *
from Project_3.patterns.observer import *
from Project_3.patterns.decorator import *
from Project_3.patterns.adapter import *
from Project_3.patterns.factory import *
from Project_3.patterns.command import *

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

def test_strategy():
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

def test_observer():
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

def test_factory():
    factory_one = Gift_basket_factory(name="Factory One")

    items = [
        Item(name="+5 Dexterity Vest", sell_in=9, quality=19, item_type=Common()),
        Item(name="Aged Brie", sell_in=1, quality=1, item_type=Aged()),
        Item(name="Elixir of the Mongoose", sell_in=4, quality=6, item_type=Common()),
    ]

    gift_basket = factory_one.create(items=items, total_quality = 200)
    assert gift_basket.get_quality() == 200

    for item in items:
        assert item in gift_basket.items

    gift_basket2 = factory_one.create(items=items, total_quality = 300)
    assert gift_basket2.get_quality() == 300

    gift_basket3 = factory_one.create(items=items, total_quality = 1000)
    assert gift_basket3.get_quality() == 1000

def test_command():

    """
    First sections tests clean by sell in attribute
    """

    items = [
        Item(name="+5 Dexterity Vest", sell_in=1, quality=19, item_type=Common()),
        Item(name="Aged Brie", sell_in=2, quality=1, item_type=Aged()),
        Item(name="Elixir of the Mongoose", sell_in=3, quality=6, item_type=Common()),
    ]

    inventory = Inventory(items=items)

    clean_command = Clean_sell_in(inventory=inventory)
    WallE = Robot(name="WallE", command=clean_command)
    WallE.execute()
    assert str(inventory.items) == "[+5 Dexterity Vest, 1, 19, Aged Brie, 2, 1, Elixir of the Mongoose, 3, 6]"

    clean_command2 = Clean_sell_in(inventory=inventory)
    inventory.update()
    WallE.command = clean_command2
    WallE.execute()
    assert str(inventory.items) == "[Aged Brie, 1, 2, Elixir of the Mongoose, 2, 5]"

    clean_command3 = Clean_sell_in(inventory=inventory)
    inventory.update()
    WallE.command = clean_command3
    WallE.execute()
    assert str(inventory.items) == "[Elixir of the Mongoose, 1, 4]"

    WallE.undo()
    assert str(inventory.items) == "[Aged Brie, 0, 3, Elixir of the Mongoose, 1, 4]"

    WallE.command = clean_command2
    WallE.undo()
    assert str(inventory.items) == "[+5 Dexterity Vest, 0, 17, Aged Brie, 0, 3, Elixir of the Mongoose, 1, 4]"

    """
    Second Sections test clean by quality
    """

    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=1, item_type=Common()),
        Item(name="Elixir of the Mongoose", sell_in=20, quality=2, item_type=Common()),
        Item(name="Aged Brie", sell_in=20, quality=1, item_type=Aged()),
    ]

    inventory = Inventory(items=items)

    clean_command = Clean_quality(inventory=inventory)
    WallE = Robot(name="WallE", command=clean_command)
    WallE.execute()
    assert str(inventory.items) == "[+5 Dexterity Vest, 10, 1, Elixir of the Mongoose, 20, 2, Aged Brie, 20, 1]"

    clean_command2 = Clean_quality(inventory=inventory)
    inventory.update()
    WallE.command = clean_command2
    WallE.execute()
    assert str(inventory.items) == "[Elixir of the Mongoose, 19, 1, Aged Brie, 19, 2]"

    clean_command3 = Clean_quality(inventory=inventory)
    inventory.update()
    WallE.command = clean_command3
    WallE.execute()
    assert str(inventory.items) == "[Aged Brie, 18, 3]"

    WallE.undo()
    assert str(inventory.items) == "[Elixir of the Mongoose, 18, 0, Aged Brie, 18, 3]"

    WallE.command = clean_command2
    WallE.undo()
    assert str(inventory.items) == "[+5 Dexterity Vest, 9, 0, Elixir of the Mongoose, 18, 0, Aged Brie, 18, 3]"
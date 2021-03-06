import pytest
from gilded_rose import Item, GildedRose
"""
Global item list for testing. 
"""
items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=27),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=42),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=49),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6)]

@pytest.fixture
def test_load():
    gild_rose = GildedRose(items)
    return gild_rose

def test_update_quality(test_load):
    test_load.update_quality()
    new_items =[
             Item(name="+5 Dexterity Vest", sell_in=9, quality=19),
             Item(name="Aged Brie", sell_in=1, quality=1),
             Item(name="Elixir of the Mongoose", sell_in=4, quality=6),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=14, quality=21),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=29),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=45),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=50),
             Item(name="Conjured Mana Cake", sell_in=2, quality=5)]
    assert test_load.items == new_items
# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):


    """ Regular Items """
    def test_regular_item_quality_normal(self):
        # Arrange
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]

        # Act
        gilded_rose = GildedRose(items)
        old = Item(name=items[0].name, sell_in=items[0].sell_in, quality=items[0].quality)
        gilded_rose.update_quality()
        new = items[0]

        # Assert
        self.assertEqual(len(items), 1)
        self.assertEqual((old.sell_in - new.sell_in), 1)
        self.assertEqual((old.quality - new.quality), 1)
        

    def test_regular_item_quality_expired(self):
        # Arrange
        items = [Item(name="+5 Dexterity Vest", sell_in=0, quality=20)]

        # Act
        gilded_rose = GildedRose(items)
        old = Item(name=items[0].name, sell_in=items[0].sell_in, quality=items[0].quality)
        gilded_rose.update_quality()
        new = items[0]

        # Assert
        self.assertEqual(len(items), 1)
        self.assertEqual((old.sell_in - new.sell_in), 1)
        self.assertEqual((old.quality - new.quality), 2)





    """ Brie Items """
    def test_brie_item_quality_normal(self):
        # Arrange
        items = [Item(name="Aged Brie", sell_in=2, quality=4)]

        # Act
        gilded_rose = GildedRose(items)
        old = Item(name=items[0].name, sell_in=items[0].sell_in, quality=items[0].quality)
        gilded_rose.update_quality()
        new = items[0]

        # Assert
        self.assertEqual(len(items), 1)
        self.assertEqual((old.sell_in - new.sell_in), 1)
        self.assertEqual((new.quality - old.quality), 1)
        

    def test_brie_item_quality_expired(self):
        # Arrange
        items = [Item(name="Aged Brie", sell_in=0, quality=4)]

        # Act
        gilded_rose = GildedRose(items)
        old = Item(name=items[0].name, sell_in=items[0].sell_in, quality=items[0].quality)
        gilded_rose.update_quality()
        new = items[0]

        # Assert
        self.assertEqual(len(items), 1)
        self.assertEqual((old.sell_in - new.sell_in), 1)
        self.assertEqual((new.quality - old.quality), 2)


    def test_brie_item_quality_max_quality(self):
        # Arrange
        items = [Item(name="Aged Brie", sell_in=0, quality=49)]

        # Act
        gilded_rose = GildedRose(items)
        old = Item(name=items[0].name, sell_in=items[0].sell_in, quality=items[0].quality)
        gilded_rose.update_quality()
        new = items[0]

        # Assert
        self.assertEqual(len(items), 1)
        self.assertEqual((old.sell_in - new.sell_in), 1)
        self.assertEqual((new.quality - old.quality), 1)





    """ Sulfuras Items """
    def test_sulfuras_item_quality(self):
        # Arrange
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=80)]

        # Act
        gilded_rose = GildedRose(items)
        old = Item(name=items[0].name, sell_in=items[0].sell_in, quality=items[0].quality)
        gilded_rose.update_quality()
        new = items[0]

        # Assert
        self.assertEqual(len(items), 1)
        self.assertEqual((old.sell_in - new.sell_in), 0)
        self.assertEqual((old.quality - new.quality), 0)





    """ backstage Items """
    def test_backstage_item_quality_normal(self):
        # Arrange
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]

        # Act
        gilded_rose = GildedRose(items)
        old = Item(name=items[0].name, sell_in=items[0].sell_in, quality=items[0].quality)
        gilded_rose.update_quality()
        new = items[0]

        # Assert
        self.assertEqual(len(items), 1)
        self.assertEqual((old.sell_in - new.sell_in), 1)
        self.assertEqual((new.quality - old.quality), 1)


    def test_backstage_item_quality_under_10(self):
        # Arrange
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]

        # Act
        gilded_rose = GildedRose(items)
        old = Item(name=items[0].name, sell_in=items[0].sell_in, quality=items[0].quality)
        gilded_rose.update_quality()
        new = items[0]

        # Assert
        self.assertEqual(len(items), 1)
        self.assertEqual((old.sell_in - new.sell_in), 1)
        self.assertEqual((new.quality - old.quality), 2)        


    def test_backstage_item_quality_under_5(self):
        # Arrange
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)]

        # Act
        gilded_rose = GildedRose(items)
        old = Item(name=items[0].name, sell_in=items[0].sell_in, quality=items[0].quality)
        gilded_rose.update_quality()
        new = items[0]

        # Assert
        self.assertEqual(len(items), 1)
        self.assertEqual((old.sell_in - new.sell_in), 1)
        self.assertEqual((new.quality - old.quality), 3)       


    def test_backstage_item_quality_expired(self):
        # Arrange
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=0)]

        # Act
        gilded_rose = GildedRose(items)
        old = Item(name=items[0].name, sell_in=items[0].sell_in, quality=items[0].quality)
        gilded_rose.update_quality()
        new = items[0]

        # Assert
        self.assertEqual(len(items), 1)
        self.assertEqual((old.sell_in - new.sell_in), 1)
        self.assertEqual((old.quality - new.quality), 0)


    def test_backstage_item_quality_max_quality(self):
        # Arrange
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49)]

        # Act
        gilded_rose = GildedRose(items)
        old = Item(name=items[0].name, sell_in=items[0].sell_in, quality=items[0].quality)
        gilded_rose.update_quality()
        new = items[0]

        # Assert
        self.assertEqual(len(items), 1)
        self.assertEqual((old.sell_in - new.sell_in), 1)
        self.assertEqual((new.quality - old.quality), 1)





    """ Conjured Items """
    def test_conjured_item_quality_normal(self):
        # Arrange
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]

        # Act
        gilded_rose = GildedRose(items)
        old = Item(name=items[0].name, sell_in=items[0].sell_in, quality=items[0].quality)
        gilded_rose.update_quality()
        new = items[0]

        # Assert
        self.assertEqual(len(items), 1)
        self.assertEqual((old.sell_in - new.sell_in), 1)
        self.assertEqual((old.quality - new.quality), 2)
        

    def test__conjured_item_quality_expired(self):
        # Arrange
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=6)]

        # Act
        gilded_rose = GildedRose(items)
        old = Item(name=items[0].name, sell_in=items[0].sell_in, quality=items[0].quality)
        gilded_rose.update_quality()
        new = items[0]

        # Assert
        self.assertEqual(len(items), 1)
        self.assertEqual((old.sell_in - new.sell_in), 1)
        self.assertEqual((old.quality - new.quality), 4)


    """  """
if __name__ == '__main__':
    unittest.main()

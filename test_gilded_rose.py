# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_item_name(self):
        # Arrange
        item = Item("foo", 0, 0)
        # Act
        # Assert
        self.assertEqual("foo", item.name)

    def test_item_sell_in(self):
        # Arrange
        item = Item("foo", 10, 0)
        # Act
        # Assert
        self.assertEqual(10, item.sell_in)

    def test_item_quality(self):
        # Arrange
        item = Item("foo", 0, 25)
        # Act
        # Assert
        self.assertEqual(25, item.quality)

    def test_normal_item_update_quality(self):
        # Arrange
        items = [Item("foo", 10, 25)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(24, items[0].quality)

    def test_normal_item_update_sell_in(self):
        # Arrange
        items = [Item("foo", 10, 25)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(9, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()

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

    def test_item_sell_in_ko(self):
        # Arrange
        item = Item("foo", -1, 0)
        # Act
        # Assert
        self.assertEqual(-1, item.sell_in)


if __name__ == '__main__':
    unittest.main()

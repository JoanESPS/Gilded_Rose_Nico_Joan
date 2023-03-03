# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_item_name(self):
        # Arrange
        items = [Item("foo", 0, 0)]
        # Act
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # Assert
        self.assertEqual("foo", items[0].name)
        


if __name__ == '__main__':
    unittest.main()

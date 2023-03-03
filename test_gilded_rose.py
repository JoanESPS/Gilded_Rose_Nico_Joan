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

    def test_normal_item_quality_non_negative_post_update(self):
        # Arrange
        items = [Item("foo", 10, 0)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(0, items[0].quality)

    def test_normal_item_quality_baisse_de_deux_quand_sell_in_zero(self):
        # Arrange
        items = [Item("foo", 0, 10)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(8, items[0].quality)

    def test_brie_quality_post_update(self):
        # Arrange
        items = [Item("Aged Brie", 10, 25)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(26, items[0].quality)

    def test_brie_quality_limitee_a_50(self):
        # Arrange
        items = [Item("Aged Brie", 10, 50)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_pas_de_changement_de_quality_post_update(self):
        # Arrange
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_pas_de_changement_de_sell_in_post_update(self):
        # Arrange
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(10, items[0].sell_in)




if __name__ == '__main__':
    unittest.main()

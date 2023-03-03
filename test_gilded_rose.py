# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose, SulfurasItem, NormalItem, BackstagePassItem, AgedBrieItem


class GildedRoseTest(unittest.TestCase):
    def test_item_name(self):
        # Arrange
        item = NormalItem("foo", 0, 0)
        # Act
        # Assert
        self.assertEqual("foo", item.name)

    def test_item_sell_in(self):
        # Arrange
        item = NormalItem("foo", 10, 0)
        # Act
        # Assert
        self.assertEqual(10, item.sell_in)

    def test_item_quality(self):
        # Arrange
        item = NormalItem("foo", 0, 25)
        # Act
        # Assert
        self.assertEqual(25, item.quality)

    def test_normal_item_update_quality(self):
        # Arrange
        items = [NormalItem("foo", 10, 25)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(24, items[0].quality)

    def test_normal_item_update_sell_in(self):
        # Arrange
        items = [NormalItem("foo", 10, 25)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(9, items[0].sell_in)

    def test_normal_item_quality_non_negative_post_update(self):
        # Arrange
        items = [NormalItem("foo", 10, 0)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(0, items[0].quality)

    def test_normal_item_quality_baisse_de_deux_quand_sell_in_zero(self):
        # Arrange
        items = [NormalItem("foo", 0, 10)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(8, items[0].quality)

    def test_brie_quality_post_update(self):
        # Arrange
        items = [AgedBrieItem(10, 25)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(26, items[0].quality)

    def test_brie_quality_limitee_a_50(self):
        # Arrange
        items = [AgedBrieItem(10, 50)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_pas_de_changement_de_quality_post_update(self):
        # Arrange
        items = [SulfurasItem()]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_pas_de_changement_de_sell_in_post_update(self):
        # Arrange
        items = [SulfurasItem()]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(1000, items[0].sell_in)

    def test_backstage_passes_quality_augmente_de_1_avec_sell_in_superieur_a_10(self):
        # Arrange
        items = [BackstagePassItem(11, 30)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(31, items[0].quality)

    def test_backstage_passes_quality_augmente_de_2_avec_sell_in_inferieur_a_10(self):
        # Arrange
        items = [BackstagePassItem(10, 30)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(32, items[0].quality)

    def test_backstage_passes_quality_augmente_de_3_avec_sell_in_inferieur_a_5(self):
        # Arrange
        items = [BackstagePassItem(5, 30)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(33, items[0].quality)

    def test_backstage_passes_quality_passe_a_0_avec_sell_in_inferieur_a_0(self):
        # Arrange
        items = [BackstagePassItem(0, 30)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(0, items[0].quality)

    def test_backstage_passes_quality_limitee_a_50(self):
        # Arrange
        items = [BackstagePassItem(5, 49)]
        guild = GildedRose(items)
        # Act
        guild.update_quality()
        # Assert
        self.assertEqual(50, items[0].quality)

if __name__ == '__main__':
    unittest.main()

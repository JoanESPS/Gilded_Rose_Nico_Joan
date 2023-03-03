# -*- coding: utf-8 -*-
from abc import abstractmethod, ABC

MAX_QUALITY = 50
MIN_QUALITY = 0
BACKSTAGE_SELL_IN_PREVENTE = 11
BACKSTAGE_SELL_IN_LAST_MINUTE = 6
BACKSTAGE_SELL_IN_AFTER_CONCERT = 0
BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class SulfurasItem(Item):
    def __init__(self):
        super().__init__("Sulfuras, Hand of Ragnaros", 1000, 80)

    def update_quality(self):
        pass


class AgedBrieItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)

    def update_quality(self):
        self.sell_in -= 1
        if self.quality < MAX_QUALITY:
            self.quality += 1


class BackstagePassItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)
        self.prevente = 10
        self.last_minute = 5
        self.after_concert = 0

    def update_quality(self):
        if self.sell_in > self.prevente:
            self.quality += 1
        elif self.last_minute < self.sell_in <= self.prevente:
            self.quality += 2
        elif self.after_concert < self.sell_in <= self.last_minute:
            self.quality += 3
        else:
            self.quality = 0

        if self.quality > MAX_QUALITY:
            self.quality = MAX_QUALITY

        self.sell_in -= 1


class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.sell_in < 0:
            self.quality -= 2
        else:
            self.quality -= 1
        if self.quality < 0:
            self.quality = 0
        self.sell_in -= 1


items = [NormalItem("abc", 5, 5), NormalItem("abc", 5, 0), AgedBrieItem(10, 10), AgedBrieItem(10, 50),
         BackstagePassItem(20, 10), BackstagePassItem(10, 10), BackstagePassItem(5, 10), BackstagePassItem(-1, 10),
         SulfurasItem(), BackstagePassItem(11, 30)]
print(items)
gildes = GildedRose(items)
gildes.update_quality()
print(items)

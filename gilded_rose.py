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


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    @abstractmethod
    def update_quality(self):
        for item in self.items:
            if item.name not in [BRIE, BACKSTAGE_PASSES, SULFURAS]:
                if item.quality > MIN_QUALITY:
                    item.quality -= 1
            else:
                if item.quality < MAX_QUALITY:
                    item.quality += 1
                    if item.name == BACKSTAGE_PASSES:
                        if item.sell_in < BACKSTAGE_SELL_IN_PREVENTE:
                            if item.quality < MAX_QUALITY:
                                item.quality += 1
                        if item.sell_in < BACKSTAGE_SELL_IN_LAST_MINUTE:
                            if item.quality < MAX_QUALITY:
                                item.quality += 1
            if item.name != SULFURAS:
                item.sell_in -= 1
            if item.sell_in < 0:
                if item.name != BRIE:
                    if item.name != BACKSTAGE_PASSES:
                        if item.quality > MIN_QUALITY:
                            if item.name != SULFURAS:
                                item.quality -= 1
                    else:
                        item.quality = 0
                else:
                    if item.quality < MAX_QUALITY:
                        item.quality += 1


class SulfurasItem(Item, GildedRose):
    def __init__(self):
        super().__init__("Sulfuras, Hand of Ragnaros", 1000, 80)

    def update_quality(self):
        pass


class AgedBrieItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)

    def update_quality(self):
        pass


class BackstagePassItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)

    def update_quality(self):
        pass


class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        pass


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    @abstractmethod
    def update_quality(self):
        for item in self.items:
            if item.name not in [BRIE, BACKSTAGE_PASSES, SULFURAS]:
                if item.quality > MIN_QUALITY:
                    item.quality -= 1
            else:
                if item.quality < MAX_QUALITY:
                    item.quality += 1
                    if item.name == BACKSTAGE_PASSES:
                        if item.sell_in < BACKSTAGE_SELL_IN_PREVENTE:
                            if item.quality < MAX_QUALITY:
                                item.quality += 1
                        if item.sell_in < BACKSTAGE_SELL_IN_LAST_MINUTE:
                            if item.quality < MAX_QUALITY:
                                item.quality += 1
            if item.name != SULFURAS:
                item.sell_in -= 1
            if item.sell_in < 0:
                if item.name != BRIE:
                    if item.name != BACKSTAGE_PASSES:
                        if item.quality > MIN_QUALITY:
                            if item.name != SULFURAS:
                                item.quality -= 1
                    else:
                        item.quality = 0
                else:
                    if item.quality < MAX_QUALITY:
                        item.quality += 1


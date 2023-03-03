# -*- coding: utf-8 -*-
from abc import abstractmethod, ABC

MAX_QUALITY = 50
MIN_QUALITY = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Shop:

    def __init__(self, items):
        self.items = items

    def update(self):
        for item in self.items:
            item.update()


class SulfurasItem(Item):
    def __init__(self):
        super().__init__("Sulfuras, Hand of Ragnaros", 1000, 80)

    def update(self):
        pass


class AgedBrieItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)

    def update(self):
        self.sell_in -= 1
        if self.quality < MAX_QUALITY:
            self.quality += 1


class BackstagePassItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)
        self.prevente = 10
        self.last_minute = 5
        self.after_concert = 0

    def update(self):
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

    def update(self):
        if self.sell_in < 0:
            self.quality -= 2
        else:
            self.quality -= 1
        if self.quality < 0:
            self.quality = 0
        self.sell_in -= 1

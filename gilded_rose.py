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

    def update_all_items_in_shop(self):
        for item in self.items:
            item.update_item()


class SulfurasItem(Item):
    def __init__(self):
        super().__init__("Sulfuras, Hand of Ragnaros", "Not for sale !", 80)

    def update_item(self):
        pass


class AgedBrieItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)

    def update_item(self):
        self.sell_in -= 1
        if self.quality < MAX_QUALITY:
            self.quality += 1


class BackstagePassItem(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)
        self.is_presale = 5 < self.sell_in <= 10
        self.is_last_minute = 0 <= self.sell_in <= 5
        self.is_after_concert = self.sell_in < 0

    def update_item(self):
        if self.is_presale:
            self.quality += 2
        elif self.is_last_minute:
            self.quality += 3
        elif self.is_after_concert:
            self.quality = 0
        else:
            self.quality += 1

        if self.quality > MAX_QUALITY:
            self.quality = MAX_QUALITY

        self.sell_in -= 1


class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_item(self):
        if self.sell_in < 0:
            self.quality -= 2
        else:
            self.quality -= 1
        if self.quality < 0:
            self.quality = 0
        self.sell_in -= 1


class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_item(self):
        if self.sell_in < 0:
            self.quality -= 4
        else:
            self.quality -= 2
        if self.quality < 0:
            self.quality = 0
        self.sell_in -= 1

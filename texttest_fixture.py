# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from gilded_rose import *

if __name__ == "__main__":
    print("OMGHAI!")
    items = [
             NormalItem(name="+5 Dexterity Vest", sell_in=10, quality=20),
             AgedBrieItem(sell_in=2, quality=0),
             NormalItem(name="Elixir of the Mongoose", sell_in=5, quality=7),
             SulfurasItem(),
             BackstagePassItem(sell_in=15, quality=20),
             BackstagePassItem(sell_in=10, quality=49),
             BackstagePassItem(sell_in=5, quality=49),
             ConjuredItem(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 5
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        Shop(items).update_all_items_in_shop()

# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Sulfuras doesn't change
            self.update_item_quality(item)
            item.sell_in -= 1
            self.handle_expired_item(item)

    def update_item_quality(self, item):
        if item.name == "Aged Brie":
            self.increase_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_pass_quality(item)
        elif item.name == "Conjured Mana Cake":
            self.decrease_quality(item, amount=2)
        else:
            self.decrease_quality(item)

    def handle_expired_item(self, item):
        if item.sell_in < 0:
            if item.name == "Aged Brie":
                self.increase_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = 0
            elif item.name == "Conjured Mana Cake":
                self.decrease_quality(item, amount=2)
            else:
                self.decrease_quality(item)

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def decrease_quality(self, item, amount=1):
        if item.quality > 0:
            item.quality -= amount

    def update_backstage_pass_quality(self, item):
        self.increase_quality(item)
        if item.sell_in < 11:
            self.increase_quality(item)
        if item.sell_in < 6:
            self.increase_quality(item)





class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

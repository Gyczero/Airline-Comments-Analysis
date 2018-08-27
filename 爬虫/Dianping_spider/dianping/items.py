# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DianpingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    time = scrapy.Field()
    desc = scrapy.Field()
    user_id = scrapy.Field()
    airline = scrapy.Field()
    estar = scrapy.Field()

    pass

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SentdexItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ticker = scrapy.Field()
    name = scrapy.Field()
    volumne = scrapy.Field()
    sent = scrapy.Field()
    delta = scrapy.Field()

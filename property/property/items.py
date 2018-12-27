# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item, Field



class JiwuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    price = Field()
    address = Field()
    lng = Field()
    lat = Field()

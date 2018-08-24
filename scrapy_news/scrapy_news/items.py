# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SoccerNewsItem(scrapy.Item):
    url = scrapy.Field()
    headline = scrapy.Field()
    subhead = scrapy.Field()
    body_text = scrapy.Field()
    author = scrapy.Field()
    datetime = scrapy.Field()
    source = scrapy.Field()
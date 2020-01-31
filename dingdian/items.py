# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    book_anthor = scrapy.Field()
    book_type = scrapy.Field()
    book_status = scrapy.Field()
    book_words = scrapy.Field()
    book_time = scrapy.Field()
    book_click_nums = scrapy.Field()

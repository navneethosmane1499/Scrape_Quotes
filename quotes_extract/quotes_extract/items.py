# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesExtractItem(scrapy.Item):
    # define the fields for your item here like:
    quote = scrapy.Field()
    quote_author = scrapy.Field()
    quote_tag = scrapy.Field()
    quote_url = scrapy.Field()

# class authorExtractItem(scrapy.Item):
#     author_name = scrapy.Field()
#     author_born_date = scrapy.Field()
#     author_bio = scrapy.Field()
#     author_url = scrapy.Field()


# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field
from scrapy.loader import ItemLoader

from scrapy.loader.processors import Identity, Compose, MapCompose, TakeFirst, Join

from dateutil.parser import parse as dateutil_parse
from w3lib.html import remove_tags


class GoodreadsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    body = Field()
    author = Field()
    num_like = Field()
    tags = Field(output_processor=Compose(set, list))

class QuotePage(scrapy.Item):
    """
    一页
    """
    quoteList = Field(output_processor=Compose(set, list))

class QuoteLoader(ItemLoader):
    # default_output_processor = TakeFirst()
    pass
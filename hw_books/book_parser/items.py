# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookParserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    item_ref = scrapy.Field()
    item_name = scrapy.Field()
    item_autors = scrapy.Field()
    item_price = scrapy.Field()
    item_disc = scrapy.Field()
    item_rating = scrapy.Field()
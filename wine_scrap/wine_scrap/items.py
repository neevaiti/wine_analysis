# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from wine_scrap.items import WineNotation


class WineScrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WineNotation(scrapy.Item):
    year = scrapy.Field()
    rating = scrapy.Field()
    wine = scrapy.Field()
    
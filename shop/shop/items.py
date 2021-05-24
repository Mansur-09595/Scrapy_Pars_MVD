# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def remove_link(value):
    return value.replace("/news", "https://гибдд.рф/news").strip()

def remove_date(value):
    return value.replace(" ", "").strip()

def remove_title(value):
    return value.replace(" ", "_").strip()

class ShopItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field(input_processor = MapCompose(remove_tags, remove_link), output_processor = TakeFirst())
    date = scrapy.Field(input_processor = MapCompose(remove_tags, remove_date), output_processor = TakeFirst())
    title = scrapy.Field(input_processor = MapCompose(remove_tags, remove_title), output_processor = TakeFirst())
    #news = scrapy.Field()

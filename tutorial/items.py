# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# define variable use scrapy.Field()
class DoubanMovieItem(scrapy.Item):

    pic = scrapy.Field()
    title = scrapy.Field()
    quote = scrapy.Field()

    # def __init__(self,pic,title,quote):
    #     self.pic = pic
    #     self.title = title
    #     self.quote = quote

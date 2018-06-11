# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HubItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pic = scrapy.Field()  # 图片
    code = scrapy.Field()  # 车牌号
    actor = scrapy.Field()  # 演员
    lenth_of_time = scrapy.Field()  # 时长
    publisher = scrapy.Field()  # 片商
    tags = scrapy.Field()  # 类别
    src = scrapy.Field()  # 链接
    alt = scrapy.Field  # 图片名字
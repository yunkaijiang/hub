# -*- coding: utf-8 -*-
import scrapy


class JavlogSpider(scrapy.Spider):
    name = 'javlog'
    allowed_domains = ['javlog.com']
    urls = 'https://javlog.com/cn/page/'
    offset = 1
    start_urls = [urls + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[]")

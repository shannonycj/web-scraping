# -*- coding: utf-8 -*-
import scrapy


class DeepLearningSpider(scrapy.Spider):
    name = 'deep_learning'
    allowed_domains = ['www.deeplearningbook.org']
    start_urls = ['http://www.deeplearningbook.org/']

    def parse(self, response):
        pass

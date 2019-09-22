# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from sentdex.items import SentdexItem
import pandas as pd
import datetime


class UsStocksSpider(scrapy.Spider):
    name = 'us_stocks'
    allowed_domains = ['sentdex.com/financial-analysis/']
    start_urls = ['http://sentdex.com/financial-analysis//']

    def parse(self, response):
        all_assets = response.xpath('//*[@id="fulltable"]/tbody/tr')
        for asset in all_assets:
            loader = ItemLoader(item=SentdexItem(), response=response)
            loader.add_value('ticker', asset.xpath('./td[1]/text()').extract_first())
            loader.add_value('name', asset.xpath('./td[2]/text()').extract_first())
            loader.add_value('volumne', asset.xpath('./td[3]/text()').extract_first())
            loader.add_value('sent', asset.xpath('./td[4]/button/text()').extract_first())
            delta_icon = asset.xpath('./td[5]/span/@class').extract_first()
            if 'up' in delta_icon:
                loader.add_value('delta', 'Up')
            else:
                loader.add_value('delta', 'Down')
            yield loader.load_item()
# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import datetime


class UsStocksSpider(scrapy.Spider):
    name = 'us_stocks'
    allowed_domains = ['sentdex.com/financial-analysis/']
    start_urls = ['http://sentdex.com/financial-analysis//']

    def parse(self, response):
        all_items = response.xpath('//*[@id="fulltable"]/tbody/tr')
        ticker = []; name = []; volumne = []; sent = []; delta = []
        for item in all_items:
            ticker.append(item.xpath('./td[1]/text()').extract_first())
            name.append(item.xpath('./td[2]/text()').extract_first())
            volumne.append(item.xpath('./td[3]/text()').extract_first())
            sent.append(item.xpath('./td[4]/button/text()').extract_first())
            delta_icon = item.xpath('./td[5]/span/@class').extract_first()
            if 'up' in delta_icon:
                delta.append('Up')
            else:
                delta.append('Down')
        
        df = pd.DataFrame(dict(list(zip(['ticker', 'name', 'volumne', 'sentiment', 'sentiment change'], \
                                                                [ticker, name, volumne, sent, delta]))))
        time_tag = str(datetime.date.today())
        df.to_csv(f'us_stocks_sent_{time_tag}.csv', index=False)
        yield 'Okay'
# -*- coding: utf-8 -*-

import scrapy
import logging
import json

from w3lib.html import remove_tags,replace_escape_chars

from dianping.items import DianpingItem

from scrapy.selector import Selector



# 爬取时间4.7

class WeiboSpider(scrapy.Spider):
    name = 'chunqiuSpider'

    allowed_domains = ['www.dianping.com']

    url_start = 'http://www.dianping.com/shop/1971319/review_all?pageno='

    start_urls = [
        url_start + '1'
    ]

    maxPage = 41

    def __init__(self, num = 41 , *args, **kwargs):
        super(WeiboSpider, self).__init__(*args, **kwargs)
        self.num = int(num)


    # deal with the work that if a weibo post does not have comment, there is no 'comment' key
    # def etl(self, d, k, keys):
    #     if k in keys and d[k] != None:
    #         return d[k]
    #     return 0


    # from Nth posts to save data
    def parseResponse(self, response, N):

        selector = Selector(response)

        infos = selector.xpath('//li/div[2]')

        for info in infos:

            item = DianpingItem()
            rank = info.xpath('div[1]/span/@title').extract()
            # time = info.xpath('div[3]/span/text()').extract()
            desc = info.xpath('div[2]/div/text()').extract()
            airline = info.xpath('div[3]/h2/text()').extract()

            item['estar'] = rank
            # item['time'] = time
            item['desc'] = replace_escape_chars(remove_tags(desc[0]),
                        which_ones=('\n', '\t', '\r',' '))
            item['airline'] = airline
            yield item


    def parse_other(self, response):
        items = self.parseResponse(response, 0)
        for item in items:
            yield item

    def parse(self, response):

        # do page 1
        logging.warning('do page1.')
        items = self.parseResponse(response, 0)
        for item in items:
            yield item

        #  # do others Pages
        #       # requests are scheduled and processed asynchronously
        for i in range(2, min(self.maxPage, self.num) + 1):
            yield scrapy.Request(self.url_start + str(i), self.parse_other)


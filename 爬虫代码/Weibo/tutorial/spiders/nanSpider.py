# -*- coding: utf-8 -*-

import scrapy
import logging
import json

from w3lib.html import remove_tags,replace_escape_chars

from tutorial.items import PostItem



# 抓取数据时间 2017年4月6日 星期四

class WeiboSpider(scrapy.Spider):
    airline_name = '南航'
    name = 'nanSpider'


    allowed_domains = ['m.weibo.cn']


    # airline_dict = {'东航': 'http://m.weibo.cn/container/getIndex?type=all&queryVal=%E4%B8%9C%E8%88%AA&luicode=10000011&lfid=106003type%3D1&title=%E4%B8%9C%E8%88%AA&containerid=100103type%3D1%26q%3D%E4%B8%9C%E8%88%AA&page=',
    #                 '国航': 'http://m.weibo.cn/container/getIndex?type=all&queryVal=%E5%9B%BD%E8%88%AA&luicode=10000011&lfid=106003type%3D1&title=%E5%9B%BD%E8%88%AA&containerid=100103type%3D1%26q%3D%E5%9B%BD%E8%88%AA&page=',
    #                 '南航': 'http://m.weibo.cn/container/getIndex?type=all&queryVal=%E5%8D%97%E8%88%AA&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%9B%BD%E8%88%AA&title=%E5%8D%97%E8%88%AA&containerid=100103type%3D1%26q%3D%E5%8D%97%E8%88%AA&page=',
    #                 '海航': 'http://m.weibo.cn/container/getIndex?type=all&queryVal=%E6%B5%B7%E8%88%AA&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%8D%97%E8%88%AA&title=%E6%B5%B7%E8%88%AA&containerid=100103type%3D1%26q%3D%E6%B5%B7%E8%88%AA&page=',
    #                 '春秋航空': 'http://m.weibo.cn/container/getIndex?type=all&queryVal=%E6%98%A5%E7%A7%8B%E8%88%AA%E7%A9%BA&luicode=10000011&lfid=100103type%3D1%26q%3D%E4%B8%8A%E6%B5%B7%E8%88%AA%E7%A9%BA&title=%E6%98%A5%E7%A7%8B%E8%88%AA%E7%A9%BA&containerid=100103type%3D1%26q%3D%E6%98%A5%E7%A7%8B%E8%88%AA%E7%A9%BA&page=',
    #                 '国泰航空': 'http://m.weibo.cn/container/getIndex?type=all&queryVal=%E5%9B%BD%E6%B3%B0%E8%88%AA%E7%A9%BA&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%98%A5%E7%A7%8B%E8%88%AA%E7%A9%BA&title=%E5%9B%BD%E6%B3%B0%E8%88%AA%E7%A9%BA&containerid=100103type%3D1%26q%3D%E5%9B%BD%E6%B3%B0%E8%88%AA%E7%A9%BA&page='
    #                 }

    # 东航 0
    # url_start = 'http://m.weibo.cn/container/getIndex?type=all&queryVal=%E4%B8%9C%E8%88%AA&luicode=10000011&lfid=106003type%3D1&title=%E4%B8%9C%E8%88%AA&containerid=100103type%3D1%26q%3D%E4%B8%9C%E8%88%AA&page='
    #
    # 国航 1
    # url_start = 'http://m.weibo.cn/container/getIndex?type=all&queryVal=%E5%9B%BD%E8%88%AA&luicode=10000011&lfid=106003type%3D1&title=%E5%9B%BD%E8%88%AA&containerid=100103type%3D1%26q%3D%E5%9B%BD%E8%88%AA&page='
    #
    # 南航 2
    url_start = 'http://m.weibo.cn/container/getIndex?type=all&queryVal=%E5%8D%97%E8%88%AA&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%9B%BD%E8%88%AA&title=%E5%8D%97%E8%88%AA&containerid=100103type%3D1%26q%3D%E5%8D%97%E8%88%AA&page='
    #
    # 海航 3
    # url_start = 'http://m.weibo.cn/container/getIndex?type=all&queryVal=%E6%B5%B7%E8%88%AA&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%8D%97%E8%88%AA&title=%E6%B5%B7%E8%88%AA&containerid=100103type%3D1%26q%3D%E6%B5%B7%E8%88%AA&page='
    #
    # 春秋航空 4
    # url_start = 'http://m.weibo.cn/container/getIndex?type=all&queryVal=%E6%98%A5%E7%A7%8B%E8%88%AA%E7%A9%BA&luicode=10000011&lfid=100103type%3D1%26q%3D%E4%B8%8A%E6%B5%B7%E8%88%AA%E7%A9%BA&title=%E6%98%A5%E7%A7%8B%E8%88%AA%E7%A9%BA&containerid=100103type%3D1%26q%3D%E6%98%A5%E7%A7%8B%E8%88%AA%E7%A9%BA&page='

    # 国泰航空 5
    # url_start = 'http://m.weibo.cn/container/getIndex?type=all&queryVal=%E5%9B%BD%E6%B3%B0%E8%88%AA%E7%A9%BA&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%98%A5%E7%A7%8B%E8%88%AA%E7%A9%BA&title=%E5%9B%BD%E6%B3%B0%E8%88%AA%E7%A9%BA&containerid=100103type%3D1%26q%3D%E5%9B%BD%E6%B3%B0%E8%88%AA%E7%A9%BA&page='


    start_urls = [
        url_start + '1'
    ]

    maxPage = 108

    def __init__(self, num = 108 , *args, **kwargs):
        super(WeiboSpider, self).__init__(*args, **kwargs)
        self.num = int(num)


    # deal with the work that if a weibo post does not have comment, there is no 'comment' key
    def etl(self, d, k, keys):
        if k in keys and d[k] != None:
            return d[k]
        return 0


    # from Nth posts to save data
    def parseResponse(self, response, N):
        js = json.loads(response.text, encoding='utf-8')
        cardNum = len(js['cards'])
        for i in range(N, cardNum):
            cardGroupNum = len(js['cards'][i]['card_group'])
            for j in range(cardGroupNum):
                it = js['cards'][i]['card_group'][j]
                if 'mblog' in it.keys():
                    mblog = it['mblog']
                    keys = mblog.keys()
                    item = PostItem()
                    item['mblogid'] = mblog['id']
                    item['created_at'] = mblog['created_at']
                    item['comments_count'] = self.etl(
                        mblog, 'comments_count', keys)
                    item['like_count'] = self.etl(mblog, 'attitudes_count', keys)
                    item['reposts_count'] = self.etl(
                        mblog, 'reposts_count', keys)
                    item['text'] = replace_escape_chars(remove_tags(mblog['text']),
                        which_ones=('\n', '\t', '\r',' '))
                    item['scheme'] = it['scheme']
                    item['user_name'] = mblog['user']['screen_name']
                    item['user_followers'] = mblog['user']['followers_count']
                    item['user_statuses'] = mblog['user']['statuses_count']
                    item['user_gender'] = mblog['user']['gender']
                    item['airline'] = self.airline_name
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

         # do others Pages
              # requests are scheduled and processed asynchronously
        for i in range(2, min(self.maxPage, self.num) + 1):
            yield scrapy.Request(self.url_start + str(i), self.parse_other)


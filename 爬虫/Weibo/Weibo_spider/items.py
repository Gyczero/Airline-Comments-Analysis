# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field


class PostItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mblogid = Field()  # weibo id
    created_at = Field()  # 说说时间
    comments_count = Field(serializer=int)  # 评论数
    reposts_count = Field(serializer=int)  # 转发数
    like_count = Field(serializer=int)  # 点赞数
    text = Field()  # 正文内容
    scheme = Field()  # 微博地址
    # userName\fans\说说数
    user_name = Field()
    user_followers = Field()
    user_statuses = Field()
    user_gender = Field()  # user gender
    airline = Field()

    #后期处理需要用到的字段
    admin=Field()
    price=Field()
    tag=Field()
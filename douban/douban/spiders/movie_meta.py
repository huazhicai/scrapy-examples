# -*- coding: utf-8 -*-
import scrapy
import random
import string

from scrapy import Request, Spider
from ..items import MovieMeta

cursor = db.connection.cursor()

class MovieMetaSpider(scrapy.Spider):
    name = 'movie_meta'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

    def parse(self, response):
        pass

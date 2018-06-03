import re
import json

from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor as sle

from ..items import *


class DoubanBookSpider(CrawlSpider):
    name = "doubanbook"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://book.douban.com/tag/"
    ]
    rules = [
        Rule(sle(allow=("/subject/\d+$")), callback='parsse_2'),
        Rule(sle(allow=("/tag/[^/]+$")), follow=True),
        Rule(sle(allow=("/tag/$",)), follow=True)
    ]

    def parse_2(self, response):
        items = []
        sel = Selector(response)
        sites = sel.css('#wrapper')
        for site in sites:
            item = DoubanSubjectItem()
            item['title'] = site.css('h1 span::text').extract()
            item['link'] = response.url
            item['content_intro'] = site.css('#link-report .intro p::text').extract()
            items.append(item)
            print(item)
        return items

    def parse_1(self, response):
        print('parsed ' + str(response))

    def process_request(self, request):
        print('process ' + str(request))

    def closed(self, reason):
        print("DoubanBookSpider Closed:" + reason)
# -*- coding: utf-8 -*-
import scrapy
from github.items import RepositoryItem

class GetrepoSpider(scrapy.Spider):
    name = 'getrepo'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/']
    
    @property
    def start_urls(self):
        url_1 = 'https://github.com/shiyanlou?tab=repositories'
        url_2 = 'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoxOTo1NyswODowMM4FkpYw&tab=repositories'
        url_3 = 'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNVQxMTozMTowNyswODowMM4Bxrsx&tab=repositories'
        url_4 = 'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMFQxMzowMzo1MiswODowMM4BjkvL&tab=repositories'
        urls = [url_1, url_2, url_3, url_4]
        return (urls[i] for i in range(4))

    def parse(self, response):
        for course in response.css('li.public'):
            item = RepositoryItem({
                'name': course.xpath('.//h3/a/text()').re_first('[\s]*([\S]*)'),
                'update_time': course.css('relative-time::attr(datetime)').extract_first()
                })
            yield item

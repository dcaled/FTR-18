# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl 90min

class NinetyMinSpider(scrapy.Spider):
    name = '90min'
    allowed_domains = ['90min.com']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):
        url = response.url
        datetime = response.css(".post-metadata__date ::text").extract_first()
        headline = response.css("h1.post-article__post-title__title ::text").extract_first()
        subhead = ""
        author = response.css("a.post-metadata__author-name ::text").extract_first()
        body_text = " ".join(response.css(".post-content p ::text").extract())

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice
#Twt
#https://www.90min.com/es/posts/6139765-ultima-hora-el-barca-tambien-cierra-la-cesion-de-andre-gomes-con-el-everton

#Instagram
#https://www.90min.com/posts/6132601-aston-villa-announce-signing-of-atletico-madrid-goalkeeper-andre-moreira-with-love-island-tweet
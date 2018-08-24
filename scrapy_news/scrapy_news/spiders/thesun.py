# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl thesun

class TheSunSpider(scrapy.Spider):
    name = 'thesun'
    allowed_domains = ['thesun.co.uk','thesun.ie']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):

        url = response.url
        datetime = response.css(".article__published span ::text").extract_first()
        headline = response.css(".article__headline ::text").extract_first()
        subhead = response.css(".article__subdeck p ::text").extract_first()
        author = response.css("span.article__author-name ::text").extract_first()
        bt_lst = response.css(".article__content p ::text").extract()
        
        for i in range(len(bt_lst)):
            bt_lst[i] = bt_lst[i].strip()
        body_text = " ".join(bt_lst)


        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)

        yield notice

#Twt
#https://www.thesun.co.uk/sport/football/6976195/chelsea-complete-signing-mateo-kovacic-real-madrid-loan/
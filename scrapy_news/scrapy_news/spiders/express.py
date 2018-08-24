# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl express

class ExpressSpider(scrapy.Spider):
    name = 'express'
    allowed_domains = ['express.co.uk']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):

        url = response.url
        datetime = response.css("time ::attr(datetime)").extract_first()
        headline = response.css("h1 ::text").extract_first()
        subhead = response.css("h3 ::text").extract_first()
        author = response.css(".author span ::text").extract_first()
        body_text = " ".join(response.css(".text-description p ::text").extract())

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)

        yield notice

#Twt
#https://www.express.co.uk/sport/football/986847/Riyad-Mahrez-signs-Man-City-Leaked-photo-done-deal-Leicester

# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl besoccer

class BesoccerSpider(scrapy.Spider):
    name = 'besoccer'
    allowed_domains = ['besoccer.com']
    source = 'Be Soccer'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = response.css("time span.ni-date::attr(content)").extract_first()
        headline = response.css("h1.ni-title ::text").extract_first()
        subhead = response.css("p.teaser ::text").extract_first()
        author = response.css("a.ni-author ::text").extract_first()
        body_text = " ".join(response.css(".ni-text-body p ::text").extract())

        body_text = body_text.replace(subhead, "")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

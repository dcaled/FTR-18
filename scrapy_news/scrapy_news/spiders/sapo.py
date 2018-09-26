# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl sapo

class SapoSpider(scrapy.Spider):
    name = 'sapo'
    allowed_domains = ['sapo.pt']
    source = 'Sapo'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = "".join(response.css(".article-metadata .date ::text").extract())
        headline = response.css("h1.article-title ::text").extract_first()
        subhead = response.css(".article-excerpt ::text").extract_first()
        author = ""
        body_text = " ".join(response.css(".article-body ::text").extract())

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl dn

class DNSpider(scrapy.Spider):
    name = 'dn'
    allowed_domains = ['dn.pt']
    source = 'Diário de Notícias'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = response.css("time ::attr(datetime)").extract_first()
        headline = response.css(".t-af1-head-title ::text").extract_first()
        subhead = " ".join(response.css(".t-af1-head-desc ::text").extract())
        author = response.css(".t-af-info-author ::text").extract_first()
        body_text = " ".join(response.css(".t-af1-c1-body p ::text").extract())

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice
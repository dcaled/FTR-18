# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl futebol365

class Futebol365Spider(scrapy.Spider):
    name = 'futebol365'
    allowed_domains = ['futebol365.pt']
    source = 'Futebol 365'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        headline = response.css(".titulo ::text").extract_first()
        subhead = response.css(".texto span.negrito ::text").extract_first()
        
        date_author = response.css(".data ::text").extract_first().split(",")
        author = date_author[0].replace("por", "")
        datetime = date_author[1]

        body_text = " ".join(response.css(".texto p ::text").extract())
        body_text = body_text.replace(subhead, "")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl eldesmarque

class ElDesmarqueSpider(scrapy.Spider):
    name = 'eldesmarque'
    allowed_domains = ['eldesmarque.com']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):
        url = response.url
        datetime = response.css(".fecha ::text").extract_first()
        headline = response.css("h1.titulo ::text").extract_first()
        subhead = ""
        author = response.css(".autor span ::text").extract_first()
        body_text = " ".join(response.css("#cuerpo-noticia p ::text").extract())

        script_text = " ".join(response.css("#cuerpo-noticia p script ::text").extract())
        body_text = body_text.replace(script_text, "")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl ecodiario

class EcoDiarioSpider(scrapy.Spider):
    name = 'ecodiario'
    allowed_domains = ['ecodiario.eleconomista.es']
    source = 'Eco Diario'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = response.css(".f-fecha ::text").extract_first()
        headline = response.css("h1 ::text").extract_first()
        subhead = " ".join(response.css(".sumarios ::text").extract())
        author = response.css(".f-autor a ::text").extract_first()
        body_text = " ".join(response.css(".noticia-cuerpo p ::text").extract())

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice


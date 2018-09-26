# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl elpais

class ElPaisSpider(scrapy.Spider):
    name = 'elpais'
    allowed_domains = ['elpais.com']
    source = 'El País'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = response.css(".articulo-actualizado ::attr(datetime)").extract_first()
        headline = response.css(".articulo-titulo ::text").extract_first()
        subhead = response.css(".articulo-subtitulo ::text").extract_first()
        author = " ".join(response.css(".autor-nombre ::text").extract())
        body_text = " ".join(response.css(".articulo-cuerpo p ::text").extract())

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

#Twt
#https://elpais.com/deportes/2018/08/24/actualidad/1535133090_339849.html
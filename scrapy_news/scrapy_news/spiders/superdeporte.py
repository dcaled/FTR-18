# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl superdeporte

class SuperdeporteSpider(scrapy.Spider):
    name = 'superdeporte'
    allowed_domains = ['superdeporte.es/valencia']
    source = 'Superdeporte'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = response.css(".fecha_hora ::text").extract_first()
        headline = response.css(".noticia h1 ::text").extract_first()
        subhead = response.css(".noticia h2 ::text").extract_first()
        author = " ".join(response.css(".autor_sup a ::text").extract())
        body_text = " ".join(response.css(".cuerpo_noticia p ::text").extract())

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

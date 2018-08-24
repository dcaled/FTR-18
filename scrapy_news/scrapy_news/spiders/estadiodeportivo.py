# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl estadiodeportivo

class EstadioDeportivoSpider(scrapy.Spider):
    name = 'estadiodeportivo'
    allowed_domains = ['estadiodeportivo.com']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):
        url = response.url
        datetime = response.css("span.fecha_hora ::text").extract_first()
        headline = response.css(".noticia h1 ::text").extract_first()
        subhead = ""
        author = response.css("span.autor_sup ::text").extract_first()
        body_text = " ".join(response.css(".cuerpo_noticia p ::text").extract())
        twt_text = " ".join(response.css(".twitter-tweet p ::text").extract())

        body_text = body_text.replace(twt_text, "")
        
        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

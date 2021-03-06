# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl abola

class ABolaSpider(scrapy.Spider):
    name = 'abola'
    allowed_domains = ['abola.pt']
    source = 'A Bola'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):

        url = response.url
        datetime = response.css(".data-hora span ::text").extract_first()
        headline = response.css("h1.titulo ::text").extract_first()
        subhead = ""
        author = response.css(".assinatura span ::text").extract_first()
        body_text = " ".join(response.css(".corpo-noticia ::text").extract())

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

#Twt
#https://www.abola.pt/Clubes/Noticias/Ver/739766/42
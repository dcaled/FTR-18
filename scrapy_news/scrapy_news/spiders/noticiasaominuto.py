# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl noticiasaominuto

class NoticiasAoMinutoSpider(scrapy.Spider):
    name = 'noticiasaominuto'
    allowed_domains = ['noticiasaominuto.com']
    source = 'Notícias ao Minuto'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):
        url = response.url
        datetime = response.css(".news-info-time ::text").extract_first()
        headline = response.css(".news-headline ::text").extract_first()
        subhead = response.css(".news-subheadline ::text").extract_first()
        author = response.css(".author-hover ::text").extract_first()
        body_text = " ".join(response.css(".news-main-text p ::text").extract())

        pub_text = " ".join(response.css(".news-main-text p a ::text ").extract())
        body_text = body_text.replace(pub_text, "") 

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

#Pub
#https://www.noticiasaominuto.com/desporto/1068563/fc-porto-prepara-nova-proposta-por-ntcham

#First letter.
# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl record

class RecordSpider(scrapy.Spider):
    name = 'record'
    allowed_domains = ['record.pt']
    source = 'Record'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):

        url = response.url
        datetime = response.css(".article_date ::text").extract_first()
        headline = response.css(".article_titles h1 ::text").extract_first()
        subhead = response.css(".article_titles h2 ::text").extract_first()
        author = response.css(".texto_autor ::text").extract_first()
        body_text = " ".join(response.css(".text_container ::text").extract())

        script_lst = response.css(".text_container script ::text").extract()
        rel_text = " ".join(response.css(".text_container .relacionadas ::text").extract())
        #twt_lst = response.css(".twitter-tweet ::text").extract()

        body_text = body_text.replace(rel_text, "")
        body_text = body_text.replace("\r\n Continuar a ler", "")
        
        for i in script_lst:
            body_text = body_text.replace(i.strip(), "")

        #body_text = body_text.replace("\n", "").replace("\r", "")
        
        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)

        yield notice

#Twt
#https://www.record.pt/internacional/paises/inglaterra/detalhe/everton-oficializa-contratacao-de-lucas-digne
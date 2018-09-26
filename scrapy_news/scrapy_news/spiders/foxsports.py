# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl foxsports

class FoxSportsSpider(scrapy.Spider):
    name = 'foxsports'
    allowed_domains = ['foxsports.com.br']
    source = 'Fox Sports'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):

        #Extract only portuguese news:
        if 'foxsports.com.br' in response.url:
            url = response.url
            datetime = response.css(".publish-date ::text").extract_first()
            headline = response.css("h1 ::text").extract_first()
            subhead = response.css("h2 ::text").extract_first()
            author = response.css(".author ::text").extract_first()
            body_text = " ".join(response.css(".embed p ::text").extract())

            body_text = body_text.replace("Veja as últimas do Mercado da Bola e quem pode chegar ao seu time", "")
            body_text = body_text.split("Saiba mais: ")[0]

            notice = SoccerNewsItem(
                headline=headline, subhead=subhead, 
                author=author, body_text=body_text, 
                url=url, datetime=datetime,
                source=self.name)
            
            yield notice



#Rel text
#https://www.foxsports.com.br/news/370761-barcelona-anuncia-venda-de-aleix-vidal-para-o-sevilla
# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl as

class DiarioAsSpider(scrapy.Spider):
    name = 'diarioas'
    allowed_domains = ['as.com']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):
        url = response.url
        datetime = response.css(".art-info time::attr(datetime)").extract_first()
        headline = response.css("h1.titular-articulo ::text").extract_first()
        subhead = response.css("h2.cont-entradilla-art ::text").extract_first()
        
        author = response.css("a.art-author ::text").extract_first()
        if not author:
            author = response.css(".info-author ::text").extract_first()

        body_text = " ".join(response.css(".int-articulo p ::text").extract())

        img_text = " ".join(response.css(".txt-img-art ::text").extract())
        sum_text = " ".join(response.css(".sumario-ficha p ::text").extract())
        body_text = body_text.replace(img_text, "")
        body_text = body_text.replace(sum_text, "")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
        
        yield notice

#Twt
#https://as.com/futbol/2018/06/25/primera/1529918347_010865.html
#Mais de uma imagem
#https://en.as.com/en/2018/07/11/football/1531325690_379444.html
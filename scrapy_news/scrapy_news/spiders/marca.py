# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl marca

class MarcaSpider(scrapy.Spider):
    name = 'marca'
    allowed_domains = ['marca.com']
    source = 'Marca'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):

        url = response.url
        datetime = response.css("time ::attr(datetime)").extract_first()
        headline = response.css(".titles h1 ::text").extract_first()
        subhead = " ".join(response.css(".section-title-group ::text").extract())
        author = response.css(".author-name ::text").extract_first()
        body_text = " ".join(response.css(".row p ::text").extract())

        sub_text = " ".join(response.css(".subtitle-items p ::text").extract())
        body_text = body_text.replace(sub_text, "")

        script_text = " ".join(response.css(".row p script ::text").extract())
        body_text = body_text.replace(script_text, "")

        #cite_text = " ".join(response.css("p.cite-author ::text").extract())
        #body_text = body_text.replace(cite_text, "")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)
    
        yield notice

#Twt
#http://www.marca.com/futbol/barcelona/2018/07/09/5b3fa0b1e5fdeaec3e8b4657.html
#Citation
#http://co.marca.com/claro/futbol/colombianos-mundo/2018/07/29/5b5d95aaca474113278b45f9.html
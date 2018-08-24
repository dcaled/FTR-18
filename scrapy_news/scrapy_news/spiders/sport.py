# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl sport

class SportSpider(scrapy.Spider):
    name = 'sport'
    allowed_domains = ['sport.es', 'sport-english.com']
    start_urls = url_selector.get_urls(allowed_domains)

    def parse(self, response):

        url = response.url
        datetime = response.css(".date ::attr(datetime)").extract_first()
        headline = response.css("h1 ::text").extract_first()
        sh_lst = response.css("h2 ::text").extract()
        author =  response.css(".author-link ::text").extract_first()
        body_text = " ".join(response.css('.editor p ::text').extract())


        for i in range(len(sh_lst)):
            sh_lst[i] = sh_lst[i].strip()
        subhead = " ".join(sh_lst)

        rel_text = response.css('.relations p ::text').extract_first()
        if rel_text:
            body_text = body_text.replace(rel_text, "")
        box_text = " ".join(response.css('.box-left-55 p ::text').extract())
        body_text = body_text.replace(box_text, "")
        
        #twt_lst = response.css(".twitter-tweet ::text").extract()
        #igm_lst = response.css(".instagram-media ::text").extract()

        #for i in twt_lst:
        #    body_text = body_text.replace(i.strip(), "")

        #for i in igm_lst:
        #    body_text = body_text.replace(i.strip(), "")
       
        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)

        yield notice

#Twt
#https://www.sport.es/es/noticias/barca/las-palabras-despedida-lucas-digne-barcelona-video-6971258
#Instagram


# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl skysports

class SkysportsSpider(scrapy.Spider):
    name = 'skysports'
    allowed_domains = ['skysports.com']
    source = 'Sky Sports'
    start_urls = url_selector.get_urls(source)

    def parse(self, response):

        url = response.url
        bt_lst = []
        mkt_lst = []
        twt_lst = []

        if 'https://www.skysports.com/football/' in url:
            datetime = response.css(".article__header-date-time ::text").extract_first()
            headline = response.css(".article__long-title ::text").extract_first()
            subhead = response.css(".article__sub-title ::text").extract_first()
            author = response.css(".article__writer-name ::text").extract_first()
            bt_lst = response.css(".article__body p ::text").extract()
            mkt_lst = response.css(".widge-marketing__text ::text").extract()
            twt_lst =  response.css('.article__widge-container p ::text').extract()

        else:
            datetime = response.css('.highlight ::text').extract_first()
            headline = response.css('.text-h1 ::text').extract_first()
            subhead = response.css(".sub-title ::text").extract_first()
            bt_lst = response.css('.box .article-body p ::text').extract()

            caption_lst = response.css('.caption ::text').extract()
            if('By ' in caption_lst[1]):
                author = caption_lst[1].replace('By ', '')
            else:
                author = ""
        
        for i in range(len(bt_lst)):
            bt_lst[i] = bt_lst[i].strip()
        body_text = " ".join(bt_lst)
                
        for i in mkt_lst:
            body_text = body_text.replace(i.strip(), "")
        
        #for i in twt_lst:
        #    body_text = body_text.replace(i.strip(), "")

        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)

        yield notice


#Twt
#http://www.skysports.com/football/news/11668/11466188/chelsea-agree-to-sell-thibaut-courtois-to-real-madrid
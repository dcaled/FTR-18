# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import SoccerNewsItem
import scrapy_news.url_selector as url_selector

#to run
#scrapy crawl zerozero

class ZeroZeroSpider(scrapy.Spider):
    name = 'zerozero'
    allowed_domains = ['zerozero.pt']
    start_urls = [
    #'http://www.zerozero.pt/news.php?id=224561',
    #'http://www.zerozero.pt/news.php?id=224765',
    #'http://www.zerozero.pt/news.php?id=224817',
    #'http://www.zerozero.pt/news.php?id=224884',
    #'http://www.zerozero.pt/news.php?id=224885',
    #'http://www.zerozero.pt/news.php?id=224931',
    #'http://www.zerozero.pt/news.php?id=225032',
    #'http://www.zerozero.pt/news.php?id=225125',
    #'http://www.zerozero.pt/news.php?id=225131',
    #'http://www.zerozero.pt/news.php?id=225157',
    #'http://www.zerozero.pt/news.php?id=225158',
    #'http://www.zerozero.pt/news.php?id=225232',
    #'http://www.zerozero.pt/news.php?id=225285',
    #'http://www.zerozero.pt/news.php?id=225298',
    #'http://www.zerozero.pt/news.php?id=225300',
    #'http://www.zerozero.pt/news.php?id=225353',
    #'http://www.zerozero.pt/news.php?id=225411',
    #'http://www.zerozero.pt/news.php?id=225414',
    #'http://www.zerozero.pt/news.php?id=225489',
    #'http://www.zerozero.pt/news.php?id=225566',
    #'http://www.zerozero.pt/news.php?id=225594',
    #'http://www.zerozero.pt/news.php?id=225604',
    #'http://www.zerozero.pt/news.php?id=225628',
    #'http://www.zerozero.pt/news.php?id=225633',
    #'http://www.zerozero.pt/news.php?id=225644',
    #'http://www.zerozero.pt/news.php?id=225683',
    #'http://www.zerozero.pt/news.php?id=225745',
    #'http://www.zerozero.pt/news.php?id=225780',
    #'http://www.zerozero.pt/news.php?id=225829',
    #'http://www.zerozero.pt/news.php?id=225861',
    #'http://www.zerozero.pt/news.php?id=225868',
    #'http://www.zerozero.pt/news.php?id=225877',
    #'http://www.zerozero.pt/news.php?id=225898',
    #'http://www.zerozero.pt/news.php?id=225925',
    #'http://www.zerozero.pt/news.php?id=225963',
    #'http://www.zerozero.pt/news.php?id=226002',
    #'http://www.zerozero.pt/news.php?id=226022',
    #'http://www.zerozero.pt/news.php?id=226076',
    #'http://www.zerozero.pt/news.php?id=226091',
    #'http://www.zerozero.pt/news.php?id=226099',
    #'http://www.zerozero.pt/news.php?id=227782',
    #'http://www.zerozero.pt/news.php?id=227975',
    #'https://www.zerozero.pt/news.php?id=221971',
    #'https://www.zerozero.pt/news.php?id=222863',
    #'https://www.zerozero.pt/news.php?id=223186',
    #'https://www.zerozero.pt/news.php?id=224552',
    #'https://www.zerozero.pt/news.php?id=225125',
    #'https://www.zerozero.pt/news.php?id=225131',
    #'https://www.zerozero.pt/news.php?id=225139',
    #'https://www.zerozero.pt/news.php?id=225270',
    #'https://www.zerozero.pt/news.php?id=225327',
    #'https://www.zerozero.pt/news.php?id=225490',
    #'https://www.zerozero.pt/news.php?id=225594',
    #'https://www.zerozero.pt/news.php?id=225986',
    #'https://www.zerozero.pt/news.php?id=226306',
    #'https://www.zerozero.pt/news.php?id=226440',
    #'https://www.zerozero.pt/news.php?id=226528',
    'https://www.zerozero.pt/news.php?id=227341',
    'https://www.zerozero.pt/news.php?id=227386',
    'https://www.zerozero.pt/news.php?id=227423',
    'https://www.zerozero.pt/news.php?id=227574',
    'https://www.zerozero.pt/news.php?id=227614',
    'https://www.zerozero.pt/news.php?id=227643',
    'https://www.zerozero.pt/news.php?id=227772',
    'https://www.zerozero.pt/news.php?id=227867',
    'https://www.zerozero.pt/news.php?id=227974',
    'https://www.zerozero.pt/news.php?id=227975',
    'https://www.zerozero.pt/news.php?id=227994',
    'https://www.zerozero.pt/news.php?id=228075',
    'https://www.zerozero.pt/news.php?id=228108',
    'https://www.zerozero.pt/news.php?id=228168',


    ]

    def parse(self, response):

        url = response.url
        datetime = response.css(".timestamp ::text").extract_first()
        headline = " ".join(response.css(".title h1 ::text").extract())
        subhead = response.css(".microtitle ::text").extract_first()
        author = response.css(".authors span ::text").extract_first()
        bt_lst = response.css(".text span p ::text").extract()

        for i in range(len(bt_lst)):
            bt_lst[i] = bt_lst[i].strip()
        body_text = " ".join(bt_lst)


        notice = SoccerNewsItem(
            headline=headline, subhead=subhead, 
            author=author, body_text=body_text, 
            url=url, datetime=datetime,
            source=self.name)

        yield notice


#Twt
#http://www.zerozero.pt/news.php?id=224817
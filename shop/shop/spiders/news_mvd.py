import scrapy
from six import b
from shop.items import ShopItem
from scrapy.loader import ItemLoader

class NewsMvd(scrapy.Spider):
    name = 'news_info'
    start_urls = ["https://гибдд.рф/news"]

    def parse(self, response):
        for info in response.css('div.sl-item'):
            l = ItemLoader(item=ShopItem(), selector=info)

            l.add_css('link', 'a.news-popup.e-popup::attr(href)')
            l.add_css('date', 'div.sl-item-date')
            l.add_css('title', 'a.news-popup.e-popup')

            yield l.load_item()

        #Парсинг всех страниц
        #next_page = response.css('a.next').attrib['href']
        #if next_page is not None:
            #yield response.follow(next_page, callback=self.parse)
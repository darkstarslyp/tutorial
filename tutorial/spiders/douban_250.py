# -*- coding:utf-8 -*-
import scrapy
from tutorial.items import DoubanMovieItem
from scrapy import Request

class Douban(scrapy.Spider):
    name = "douban"
    start_urls = ['https://movie.douban.com/top250']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def parse(self, response):
        movie_list = response.xpath('//div[@id="content"]/div/div[@class="article"]/ol/li')

        if movie_list:
            for movie_item in movie_list:
                movie_pic = movie_item.xpath('div/div[@class="pic"]/a/img/@src').extract()
                movie_title = movie_item.xpath('div/div[@class="info"]/div/a/span[@class="title"]/text()').extract()
                movie_quote = movie_item.xpath('div/div[@class="info"]/div/p[@class="quote"]/span/text()').extract()

                if movie_quote:
                    movie_quote = movie_quote[0]
                if movie_title:
                    movie_title = movie_title[0]
                if movie_pic:
                    movie_pic = movie_pic[0]
                movie = DoubanMovieItem()

                movie['pic'] = movie_pic
                movie['title'] = movie_title
                movie['quote'] = movie_quote

                yield movie

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)

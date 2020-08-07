import scrapy
from scrapy.http import HtmlResponse
from book_parser.items import BookParserItem

class Book24Spider(scrapy.Spider):
    name = 'book24'
    allowed_domains = ['book24.ru']
    start_urls = ['https://book24.ru/search/?q=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5']

    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//a[@class='catalog-pagination__item _text js-pagination-catalog-item']/@href").extract()[-1]
        if 'Далее' in response.xpath("//a[@class='catalog-pagination__item _text js-pagination-catalog-item']/text()").extract():
            yield response.follow(next_page, callback=self.parse)
        books_links = response.xpath("//a[@class='book__title-link js-item-element ddl_product_link ']/@href").extract()
        for link in books_links:
            yield response.follow(link, callback=self.book_pars)
        pass

    def book_pars(self, response: HtmlResponse):
        link = response.url
        name = response.xpath('//h1/text()').extract_first()
        autor = response.xpath('//a[@class="item-tab__chars-link js-data-link"]/text()').extract_first()
        price = response.xpath("//div[@class='item-actions__prices']//b/text()").extract_first()
        disc = None
        rating = response.xpath('//span[@class="rating__rate-value"]/text()').extract_first()
        yield BookParserItem(item_ref = link,
                             item_name = name,
                             item_autors = autor,
                             item_price = price,
                             item_disc = disc,
                             item_rating = rating)
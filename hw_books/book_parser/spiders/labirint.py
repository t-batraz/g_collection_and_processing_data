import scrapy
from scrapy.http import HtmlResponse
from book_parser.items import BookParserItem


class LabirintSpider(scrapy.Spider):
    name = 'labirint'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/search/%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/?page=1']

    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//div[@class='pagination-next']//a[@class='pagination-next__text']/@href").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        books_links = response.xpath("//a[@class='product-title-link']/@href").extract()
        for link in books_links:
            yield response.follow(link, callback=self.book_pars)

    def book_pars(self, response: HtmlResponse):
        link = response.url
        name = response.xpath('//h1/text()').extract_first()
        autor = response.xpath("//div[@class='authors']/a/text()").extract_first()
        price = response.xpath("//span[@class='buying-priceold-val-number']/text()").extract_first()
        disc = response.xpath("//span[@class='buying-pricenew-val-number']/text()").extract_first()
        rating = response.xpath("//div[@id='rate']/text()").extract_first()
        yield BookParserItem(item_ref=link,
                             item_name=name,
                             item_autors=autor,
                             item_price=price,
                             item_disc=disc,
                             item_rating=rating)



#
import scrapy

class KitapyurduSpider(scrapy.Spider):
    name = 'booksky'
    allowed_domains = ['kitapyurdu.com']
    start_urls = ['https://www.kitapyurdu.com/index.php?route=product/category&filter_category_all=true&path=1_200&filter_in_stock=1&sort=purchased_365&order=DESC&limit=100&page=1']

    def parse(self, response):
        book_page_links = response.css('div.cover a::attr(href)')
        yield from response.follow_all(book_page_links, self.parse_book)

        pagination_links = response.css('.links a::attr(href)')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_book(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'cover': extract_with_css('.image img::attr(src)'),
            'title': response.xpath('/html/body/div[1]/div[7]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/h1/text()').extract_first(),
            'authors': response.xpath('/html/body/div[1]/div[7]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/span/span/span/a/span/text()').extract_first(),
            'publishedDate': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[4]/div[2]/text()').extract_first(),
            'pageCount': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[5]/div[2]/text()').extract_first(),
            'isbn': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[7]/div[2]/text()').extract_first(),
            'publisher': response.xpath('/html/body/div[1]/div[7]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[2]/span/a/span/text()').extract_first(),
            'info': response.xpath('/html/body/div[1]/div[7]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[3]/span/text()').extract_first(),            
        }
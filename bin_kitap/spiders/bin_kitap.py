import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://1000kitap.com/kitaplar?s=alfabetik&sayfa=1']

    def parse(self, response):
        book_page_links = response.css('div.resim a::attr(href)')
        yield from response.follow_all(book_page_links, self.parse_book)

        pagination_links = response.css('li.page-item a::attr(href)')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_book(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'cover': extract_with_css('.resim img::attr(src)'),
            'title': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[1]/div[2]/text()').extract_first(),
            'authors': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[2]/div[2]/a[1]/text()').extract_first(),
            'publishedDate': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[4]/div[2]/text()').extract_first(),
            'pageCount': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[5]/div[2]/text()').extract_first(),
            'isbn': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[7]/div[2]/text()').extract_first(),
            'publisher': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[11]/div[2]/text()').extract_first(),
            'info': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[12]/text()').extract_first(),            
        }
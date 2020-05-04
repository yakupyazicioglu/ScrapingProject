import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'pages'

    start_urls = ['https://1000kitap.com/kitaplar?s=alfabetik&sayfa=1',]

    def parse(self, response):
        
        next_page = response.css('li.page-item a::attr(href)')[-1].get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


       
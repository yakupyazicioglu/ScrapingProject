import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MySpider(CrawlSpider):
    name = 'wholeb'
    allowed_domains = ['1000kitap.com']
    f = open('urls.json')
    start_urls =[url.strip() for url in f.readlines()]
    f.close()

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)

        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'cover': extract_with_css('.resim img::attr(src)'),
            'title': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[1]/div[2]/text()').extract_first(),
            'authors': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[2]/div[2]/a[1]/text()').extract_first(),
            'publishedDate': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[4]/div[2]/text()').extract_first(),
            'pageCount': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[5]/div[2]/text()').extract_first(),
            'isbn': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[7]/div[2]/text()').extract_first(),
            'publisher': response.css('.publisher a::text').extract_first(),
            'category': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[7]/div[2]/text()').extract_first(),
            'info': response.xpath('/html/body/div[1]/div[4]/div[3]/div[2]/div[12]/text()').extract_first(),
        }

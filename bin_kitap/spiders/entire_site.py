import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'entires'
    allowed_domains = ['1000kitap.com']
    start_urls = ['https://1000kitap.com/kitap/']
    
    rules = (
        Rule(LinkExtractor(allow=[r'kitap/']), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=[r'kitap/\w+']), callback='parse_item', follow=True),
        
    )

    def parse_item(self, response):
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
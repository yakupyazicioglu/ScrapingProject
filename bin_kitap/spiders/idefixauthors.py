import scrapy
import uuid
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AuthorSpider(scrapy.Spider):
    name = 'idefixauthor'
    """ start_urls = ['https://www.idefix.com/yazarlar#/page=%s' % Page for Page in range(5, 12)] """
    # start_urls = ["https://www.idefix.com/yazarlar?pref=A#/page=2"]

    allowed_domains = ['https://www.idefix.com']
    start_urls = ['https://www.idefix.com/']
    
    rules = (
        Rule(LinkExtractor(allow=[r'Yazar/']), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=[r'Yazar/\w+']), callback='parse_item', follow=True),
    ) 

    def parse(self, response):
        author_page_links = response.css('.authors-list a::attr(href)').getall()
        yield from response.follow_all(author_page_links, self.parse_author)

    def parse_author(self, response):
        yield {
            'authorId': str(uuid.uuid4().hex)[:16],
            'authorName': response.css('h1::text').extract_first(),
            'cover': response.css('.full-content img::attr(data-src)').extract_first(),
            'summary': response.css('.full-content p::text').extract_first(),
        }

# scrapy crawl idefixauthors -o idefixauthors.json
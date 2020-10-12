import scrapy
import re
import uuid

class AuthorSpider(scrapy.Spider):
    name = 'idefixauthors'
    start_urls = ['https://www.idefix.com/yazarlar#/page=%s' %
                  Page for Page in range(1, 12)]

    def parse(self, response):
        author_page_links = response.css('.authors-list a::attr(href)')
        yield from response.follow_all(author_page_links, self.parse_author)

    def parse_author(self, response):
        yield {
            'authorId': str(uuid.uuid4().hex)[:16],
            'authorName': response.css('h1::text').extract_first(),
            'cover': response.css('.full-content img::attr(data-src)').extract_first(),
            'summary': response.css('.full-content p::text').extract_first(),
        }

# scrapy crawl idefixauthors -o idefixauthors.json
import scrapy
import re
import uuid

class AuthorSpider(scrapy.Spider):
    name = 'idefixbooks'
    start_urls = ['https://www.idefix.com/kategori/Kitap/Egitim-Basvuru/Is-Ekonomi-Hukuk/Medya/grupno=00483?Page=%s' %
                  Page for Page in range(1, 15)]

    def parse(self, response):
        book_page_links = response.css('div.box-title a::attr(href)')
        yield from response.follow_all(book_page_links, self.parse_book)

    def parse_book(self, response):
        details = response.css('.product-info-list a::text').extract()
        str1 = ''.join(str(e) for e in details)
        isbn = re.findall(
            "[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", str(str1))
        publishedDate = re.findall("[2][0][0-2][0-9]", str(str1))

        str2 = response.css('.product-description p::text').extract()
        info = ''.join(str(e) for e in str2)

        yield {
            'id': str(uuid.uuid4()),
            'isbn': ''.join(str(e) for e in isbn),
            'title': response.css('.prodyctDetailTopTitle h1::text').extract_first().strip(),
            'authors': response.xpath('//*[@id="productpricedetails"]/div[1]/div[3]/div[1]/span[2]/a/text()').extract_first(),
            'cover': response.xpath('//*[@id="main-product-img"]/@data-src').extract_first(),
            'publisher': response.css('.publisher a::text').extract_first(),
            'publishedDate': ''.join(str(e) for e in publishedDate),
            'category': 'Medya',
            'info': info,
        }

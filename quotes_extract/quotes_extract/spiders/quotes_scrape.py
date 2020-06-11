import scrapy
from scrapy.http import FormRequest
from ..items import QuotesExtractItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'hosmanenavneet@gmail.com',
            'password': '12345678'
        }, callback= self.start_scraping)

    def start_scraping(self, response):
        all_div_quotes = response.css("div.quote")

        items = QuotesExtractItem()

        for q in all_div_quotes:
            quote = q.css('span.text::text').extract()
            author = q.css('.author::text').extract()
            tag = q.css('.tag::text').extract()

            items['quote'] = quote
            items['quote_author'] = author
            items['quote_tag'] = tag
            items['quote_url'] = response.request.url
            yield items

        # next_page = response.css('li.next a::attr(href)').get() #for pages which have next button to go to next page

        # if next_page is not None:
        #   yield response.follow(next_page, callback=self.parse)

        next_page = 'http://quotes.toscrape.com/page/' + str(QuoteSpider.page_number) + '/'
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.start_scraping)

        else :
            all_tags = response.css('div.tags-box a::text').extract()
            main_url = 'http://quotes.toscrape.com/'
            for tag in all_tags :
                url = main_url + '/tag/' + tag
                yield scrapy.Request(url, self.start_scraping)

    # def parse_author(self, response):
    #     author = authorExtractItem()
    #
    #     def extract_with_css(query):
    #         return response.css(query).get(default='').strip()
    #
    #     author['author_name'] = extract_with_css('h3.author-title::text')
    #     author['author_born_date'] = extract_with_css('.author-born-date::text')
    #     author['author_bio'] = extract_with_css('.author-description::text')
    #     author['author_url'] = response.request.url
    #     yield  author
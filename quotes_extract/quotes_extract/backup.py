import scrapy
from ..items import QuotesExtractItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        all_div_quotes = response.css("div.quote")
        items = QuotesExtractItem()
        #
        for q in all_div_quotes:
            quote = q.css('span.text::text').extract()
            author = q.css('.author::text').extract()
            tag = q.css('.tag::text').extract()

            items['quote'] = quote
            items['author'] = author
            items['tag'] = tag
            yield items

        #next_page = response.css('li.next a::attr(href)').get() #for pages which have next button to go to next page

        #if next_page is not None:
        #   yield response.follow(next_page, callback=self.parse)

        next_page = 'http://quotes.toscrape.com/page/' + str(QuoteSpider.page_number) + '/'
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)


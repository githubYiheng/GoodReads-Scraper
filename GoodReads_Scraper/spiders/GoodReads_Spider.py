import scrapy
import json
from ..items import QuoteItem, QuoteLoader, QuotePage
from bs4 import BeautifulSoup

# Initial url to crawl. CRUCIALLY, DOES NOT CONTAIN THE PAGE NUMBER.
# init_url = 'https://www.goodreads.com/author/quotes/656983.J_R_R_Tolkien?page=%s'
# init_url = 'https://www.goodreads.com/quotes/tag/life?page=%s'
init_url = 'https://www.goodreads.com/quotes?page=%s'
# Set these two variables as the (inclusive, inclusive) number of pages to crawl.
# By default, this spider will only crawl the first page.
start_page = 1
end_page = 10

class QuotesSpider(scrapy.Spider):
    name = "GoodReadsSpider"

    def start_requests(self):

        for i in range(start_page, (end_page + 1)):
            url = init_url % i
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        all_quotes = soup.findAll('div', {'class': 'quote'})
        page = QuotePage()
        quotes = []
        for q_soup in all_quotes:
            item = QuoteItem()

            text_div = q_soup.find('blockquote', {'class': 'quoteBody'})
            auchor_span = q_soup.find('span', {'class': 'quoteAuthor'})
            tags_div = q_soup.find('div', {'class': 'quoteTags'})
            likes_span = q_soup.find('span', {'class': 'likesCount'})

            if text_div:
                item['body'] = text_div.text
            if auchor_span:
                auchor: str = auchor_span.text
                item['author'] = auchor.replace('\n', '')
            if likes_span:
                item['num_like'] = likes_span.text
            if tags_div:
                tags = []
                a_array = tags_div.findAll('a')
                for a in a_array:
                    tags.append(a.text)
                item['tags'] = tags

            quotes.append(item)
        page['quoteList'] = quotes
        self.logger.info(page)
        return page

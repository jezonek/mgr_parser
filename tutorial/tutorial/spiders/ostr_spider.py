import scrapy


class QuotesSpider(scrapy.Spider):
    name = "ostr_spider"
    start_urls = [
        'https://www.tekstowo.pl/piosenki_artysty,o_s_t_r_.html'
]

    def parse(self, response):
        for song_link in response.css('div.box-przeboje a::attr(href)').re(r'piosenka.+'):
            next_page=response.urljoin(song_link)
            yield scrapy.Request(next_page, callback= self.parse)
        if response.css('div.song-text'):
            list_of_textlines= response.css('div.song-text::text').getall()

            yield {'text': ''.join(list_of_textlines)}

        # text=response.css('div.song-text::text').get()
        # yield {'text':text}
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
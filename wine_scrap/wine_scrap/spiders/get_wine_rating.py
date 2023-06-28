import scrapy
from wine_scrap.items import WineNotation


class GetWineRatingSpider(scrapy.Spider):
    name = "get_wine_rating"
    allowed_domains = ["idealwine.com"]
    start_urls = ["https://www.idealwine.com/"]

    def parse(self, response):
        rows = response.xpath('//tr[td[@class="millesime-row"]]')

        for row in rows:
            year = row.xpath('.//td[@class="millesime-row"]/a/text()').get()
            wine_ratings = row.xpath('.//td[a]/a')
            
            for rating in wine_ratings:
                region = rating.attrib['title'].split(' - ')[1]
                score = rating.xpath('./strong/text()').get()
                
                wine = WineNotation()
                wine['year'] = year
                wine['region'] = region
                wine['score'] = score
                yield wine

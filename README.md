1. 如何使用xpath?

2. 如何定义Spider Item
   ```
    # 强制标示 scrapy.Field() ，
    class DoubanMovieItem(scrapy.Item):
        pic = scrapy.Field()
        title = scrapy.Field()
        quote = scrapy.Field()

   ```
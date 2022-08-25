from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.spiders.crawler_spider import CrawlerSpider
from scrapy import signals
from scrapy.signalmanager import dispatcher
import csv

def spider_results():
    results = []
    def crawler_results(signal, sender, item, response, spider):
        results.append(item)
    dispatcher.connect(crawler_results, signal=signals.item_scraped)
    
    process = CrawlerProcess(get_project_settings())
    process.crawl(CrawlerSpider)
    process.start()


    with open('questions.csv', 'w') as csvfile:
        fieldnames = ['id', 'title', 'content', 'vote', 'answer', 'view']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in results:
            writer.writerow({'id': i['id'], 'title': i['title'], 'content': i['content'], 'vote': i['vote'], 'answer': i['answer'], 'view': i['view'],})

if __name__ == '__main__':
    print(str(spider_results()))
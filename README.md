pip install scrapy

scrapy startproject crawldata

scrapy shell https://stackoverflow.com/questions/tagged/python

scrapy crawl posts -o posts.json

pip install scrapy-xlsx

scrapy crawl posts -o posts.xlsx



docker build -t mycrawler .

docker compose up

docker cp 7554a46c321fddf841417a1696200d00fae3528e1e376718b5d4848556616174:/go-spider/questions.csv C:/Users/ACER/Symphony/CrawdataPython/crawler/questions.csv
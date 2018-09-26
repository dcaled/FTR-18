import time

#Dir with manually collected news.
man_col_path = 'manual_collection/2018_09_26/*.txt'
#Json file with consolidated manually collected news.
man_sum_path = 'manual_collection/{}_manual_col.json'.format(time.strftime("%Y_%m_%d"))
#Dir with news collected with scrapy.
scrapy_news_path = 'scrapy_collection/2018_09_26/*.json'
#Metadata file.
metadata_path = 'news_metadata/2018_09_26_news_metadata.csv'
#Merged (manually and scrapy) news collection.
merged_path = 'consolidated_collection/{}_dataset.json'.format(time.strftime("%Y_%m_%d"))

import json
import csv
import glob
import errno
import ast
import config

############ Parsing Metadata File ############

def parse_metadata(metadata_path):
    metadata = {}
    with open(metadata_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        for row in csv_reader:
            metadata[int(row[1])] = {
                'id_rumour': row[0],
                'news_source': row[2],
                'url': row[5],
                'language': row[4],
                'news_article_date': row[3],
                'headline': '',
                'subhead': '',
                'body_text': ''
            }

    return metadata

##############################################


################### Scrapy ###################

def parse_scrapy(scrapy_news_path,scrapy_news={}):
    sources = glob.glob(scrapy_news_path)   

    for source in sources:
        with open(source, encoding='utf8') as f:
            json_file = json.load(f)

        news_articles = json_file['news_articles']


        for news_article in news_articles:
            headline = news_article['headline']
            subhead = news_article['subhead']
            author = news_article['author']
            body_text = news_article['body_text']
            url = news_article['url']
            datetime = news_article['datetime']
            source = news_article['source']
            
            scrapy_news[url] = {
                'headline': headline,
                'subhead': subhead,
                'body_text': body_text
            }
    return scrapy_news


##############################################

############# Manual Collection ##############

def parse_manual(man_col_path, manual_news={}):
    with open(man_col_path, encoding='utf8') as f:
        json_file = json.load(f)

        news_articles = json_file['news_articles']

        for news_article in news_articles:
            #print(news_article)
            headline = news_article['title']
            subhead = news_article['subtitle']
            body_text = news_article['content']
            url = news_article.get('link')
            id_news_article = news_article['id_news_article']

            manual_news[int(id_news_article)] = {
                'url': url,
                'headline': headline,
                'subhead': subhead,
                'body_text': body_text
            }
    return manual_news

        
##############################################


################## Merging ###################
def merge(metadata,scrapy_news,manual_news):
    for k,v in metadata.items():
        url = metadata[k]['url']
        #mnk = manual_news.keys()
        
        if(scrapy_news.get(url)):
            if(scrapy_news[url].get('headline')):
                metadata[k]['headline'] = scrapy_news[url]['headline']
            if(scrapy_news[url].get('subhead')):
                metadata[k]['subhead'] = scrapy_news[url]['subhead']
            if(scrapy_news[url].get('body_text')):
                body_text = scrapy_news[url]['body_text']
                body_text = body_text.replace('\n', ' ').replace('\r', ' ')
                metadata[k]['body_text'] = ' '.join(body_text.split())
        elif(manual_news.get(k)):
            if(manual_news[k].get('headline')):
                metadata[k]['headline'] = manual_news[k]['headline']
            if(manual_news[k].get('subhead')):
                metadata[k]['subhead'] = manual_news[k]['subhead']
            if(manual_news[k].get('body_text')):
                metadata[k]['body_text'] = manual_news[k]['body_text']
    return metadata      


def save_merged(merged_path, parsed_news):
    news_file = open(merged_path, 'w', encoding='utf8')
    news_file.write(json.dumps(parsed_news, indent=4, ensure_ascii=False))
    news_file.close()

##############################################

################ Sanity Check ################

def check_empty_values(parsed_news):
    print('Problems found at...')
    pcount = 0
    for id_na, attrs in parsed_news.items():
        problems = []
        for k, v in attrs.items():
            if k != 'subhead' and v == '':
                problems+=[k]
                pcount+=1
        if(problems):
            #print('{}, {}, {}'.format(id_na, parsed_news[id_na]['news_source'], problems))
            print('{}, {}, {}'.format(id_na, parsed_news[id_na]['url'], problems))

    print('Total of {} problems found.'.format(pcount))



def check_missing_ids(parsed_news):
    ncount = 0
    missing = []
    keys = list(parsed_news.keys())
    for count in range(len(keys)):
        count+=1
        if(count not in keys):
            missing+=[count]

    print('Missing news: {}.'.format(missing))


def check_scrapy_error(scrapy_news):
    for k in scrapy_news.keys():
        if not scrapy_news[k]['headline']:
            print(k, 'no headline')
        if not scrapy_news[k]['body_text']:
            print(k, 'no body text')

##############################################

def main():
    
    #Setting the paths
    scrapy_news_path = config.scrapy_news_path
    metadata_path = config.metadata_path
    man_col_path = config.man_sum_path
    merged_path = config.merged_path

    #Parse news collected with scrapy.
    scrapy_news = parse_scrapy(scrapy_news_path)
    #Check if scrapy data has errors.
    check_scrapy_error(scrapy_news)
    #Parse news manually collected.
    manual_news = parse_manual(man_col_path)
    
    #Parse csv metadata.
    metadata = parse_metadata(metadata_path)
    #Merge csv metadata, scrapy news and manual news.
    parsed_news = merge(metadata, scrapy_news, manual_news)
    #Save merged data.
    save_merged(merged_path,parsed_news)

    #Check if required attributes are valid.
    check_empty_values(parsed_news)
    #Check for missing sequential ids.
    #check_missing_ids(parsed_news)

if __name__ == '__main__':
    main()

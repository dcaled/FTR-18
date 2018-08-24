# coding: utf8
from .urls import urls_list

def get_urls(allowed_domains):
    result = []
    for domain in allowed_domains:
        for url in urls_list:
            if domain in url:
                result += [url]
    return result

def main():
    print('Selecting urls...')

if __name__ == '__main__':
    main()

    

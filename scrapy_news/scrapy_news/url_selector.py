# coding: utf8
import csv
import os, sys

dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(dir_name)
import config

def get_urls(name):
    result = []
    csv_path = os.path.join(dir_name,config.metadata_path)
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            source = row[2]
            source = source.replace(' English', '')
            source = source.replace(' Spanish', '')
            source = source.replace(' Portuguese', '')
            if source == name:
                result += [row[5]]
    return result


def main():
    print('Selecting urls...')





if __name__ == '__main__':
    main()

    

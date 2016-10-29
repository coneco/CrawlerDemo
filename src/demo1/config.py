"""basic config for the crawler"""

import re

DATA_PATH = '.\\data\\raw_data.csv'

INIT_PAGE = 'https://movie.douban.com/'

FOLLOW_REG = r'https://movie\.douban\.com/.*'

DATA_REG = r'https://movie\.douban\.com/subject/\d*'

COLS = ['number', 'title', 'director', 'date', 'score']
DELIMITER = '|'

def data_string(url, soup):
    '''data_string'''
    number = url.split('/')[4]
    print('get: ' + number)

    content = soup.find(id='content')
    if content:
        info = content.find(id='info')
        title = content.h1.span.string

        director = ''
        for drct in info.find_all('span')[2].find_all('a'):
            director = director + '/' + drct.string
        director = director[1:]

        date = info.find(string=re.compile(r'^\d{4}'))
        if isinstance(date, str):
            date = date.split('(')[0]
        else:
            date = 'N/A'

        score = content.find(id='interest_sectl').strong.string
        if not score:
            score = 'N/A'
        return number + '|' + title + '|' + director + '|' + date + '|' + score + '\n'
    else:
        return number + '|N/A|N/A|N/A|N/A\n'

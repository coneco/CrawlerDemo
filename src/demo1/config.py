INIT_PAGE = "https://movie.douban.com/"

FOLLOW_REG = r"https://movie\.douban\.com/.*"

DATA_REG = r"https://movie\.douban\.com/subject/\d*"

COLS = "number,title,director,date"


def data_string(url, soup):
    number = url.split('/')[4]
    title = soup.title.string.split('(')[0]
    director = ''
    for d in soup.find(id='info').find_all('span')[2].find_all('a'):
        director = director + '/' + d.string
    director = director[1:]
    date = soup.find(id='info').find_all('span')[15].string.split('(')[0]
    print('get: ' + title)
    return number + '|' + title + '|' + director + '|' + date + '\n'

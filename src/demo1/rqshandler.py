import config

import re
from bs4 import BeautifulSoup
import requests as rqs


class RQSHandler(object):
    """docstring for RQSHandler"""

    def __init__(self, url, data_file):
        super(RQSHandler, self).__init__()
        self.url = url
        self.data_file = data_file
        self.r = rqs.get(url)
        self.soup = BeautifulSoup(self.r.text, "lxml")
        self.follow_reg = re.compile(config.FOLLOW_REG)
        self.data_reg = re.compile(config.DATA_REG)

    def get_data(self):
        if self.data_reg.match(self.url):
            self.data_file.write(config.data_string(self.url, self.soup))

    def get_nexts(self):
        for link in self.soup.find_all('a'):
            h = link.get('href')
            if type(h) == str and self.follow_reg.match(h):
                yield h

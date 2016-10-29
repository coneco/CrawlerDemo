"""docstring for moudle RQSHandler"""
import re

import config

from bs4 import BeautifulSoup
import requests as rqs


class RQSHandler(object):
    """docstring for RQSHandler"""

    def __init__(self, url, data_file):
        super(RQSHandler, self).__init__()
        self.url = url
        self.data_file = data_file
        self.request = rqs.get(url)
        self.soup = BeautifulSoup(self.request.text, "lxml")
        self.follow_reg = re.compile(config.FOLLOW_REG)
        self.data_reg = re.compile(config.DATA_REG)

    def get_data(self):
        """get_data"""
        if self.data_reg.match(self.url):
            self.data_file.write(config.data_string(self.url, self.soup))

    def get_nexts(self):
        """get_nexts"""
        for link in self.soup.find_all('a'):
            href = link.get('href')
            if isinstance(href, str) and self.follow_reg.match(href):
                if self.data_reg.match(href):
                    yield '/'.join(href.split('/')[:5]) + '/'
                else:
                    yield href

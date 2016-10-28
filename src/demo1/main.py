import queue
import requests as rqs
from bs4 import BeautifulSoup

init_page = "1"

def get_data(url):
    print(url)

def get_nexts(url):
    return ["1", "2", "3"];

url_queue = queue.Queue()
seen = set()

url_queue.put(init_page)
seen.add(init_page)

while(not url_queue.empty()): 
    cur_url = url_queue.get()
    get_data(cur_url)
    for next_url in get_nexts(cur_url):
        if next_url not in seen:
            url_queue.put(next_url)
            seen.add(next_url)

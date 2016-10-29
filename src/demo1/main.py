import config
import rqshandler

import queue

url_queue = queue.Queue()
seen = set()

url_queue.put(config.INIT_PAGE)
seen.add(config.INIT_PAGE)

f = open('.\\data\\raw_data.csv', 'w')

while(not url_queue.empty()):
    cur_url = url_queue.get()
    rqsHandler = rqshandler.RQSHandler(cur_url, f)
    rqsHandler.get_data()
    for next_url in rqsHandler.get_nexts():
        if next_url not in seen:
            url_queue.put(next_url)
            seen.add(next_url)

f.close()

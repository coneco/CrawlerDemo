"""main process of crawler"""
import queue

import config
import rqshandler


def main():
    """main"""
    url_queue = queue.Queue()
    seen = set()

    url_queue.put(config.INIT_PAGE)
    seen.add(config.INIT_PAGE)

    data_file = open(config.DATA_PATH, 'w', encoding='utf-8')
    data_file.write(config.DELIMITER.join(config.COLS) + '\n')

    while not url_queue.empty():
        cur_url = url_queue.get()
        rqs_handler = rqshandler.RQSHandler(cur_url, data_file)
        rqs_handler.get_data()
        for next_url in rqs_handler.get_nexts():
            if next_url not in seen:
                url_queue.put(next_url)
                seen.add(next_url)

    data_file.close()
    print("completed!")


if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))

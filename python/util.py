import datetime
import logging
import sys

LOG_DIR = '/home/huanchar/logs/'

class Logger:
    def myLogger(self):

        logger = logging.getLogger('huanchar_python')

        if not len(logger.handlers):
            logger.setLevel(logging.DEBUG)
            now = datetime.datetime.now()
            file_handler = logging.FileHandler(LOG_DIR + '/CharlesPython' + now.strftime('%Y-%m-%d') + '.log')
            stream_handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter('%(asctime)s [%(filename)s: %(levelname)s] %(message)s')

            file_handler.setFormatter(formatter)
            stream_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.addHandler(stream_handler)

        return logger

if __name__ == '__main__':
    log = Logger().myLogger()
    log.info('hello world')

import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def work1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


def work2(x, y=1):
    logging.debug('start')
    logging.debug(x)
    logging.debug(y)
    time.sleep(5)
    logging.debug('end')


if __name__ == '__main__':
    t1 = threading.Thread(name='rename worker1', target=work1)
    t2 = threading.Thread(target=work2, args=(100, ), kwargs={'y': 200})
    # start = time.time()
    t1.start()
    t2.start()
    # end = time.time()
    print('ALL COMPLETE')
    # print('%.3f seconds' % (end - start))
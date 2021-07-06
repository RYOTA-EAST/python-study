import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def work1(barrier):
    r = barrier.wait()
    logging.debug('num={}'.format(r))
    while True:
        logging.debug('work1 start')
        time.sleep(2)
        logging.debug('work1 end')


def work2(barrier):
    r = barrier.wait()
    logging.debug('num={}'.format(r))
    while True:
        logging.debug('work1 start')
        time.sleep(2)
        logging.debug('work1 end')


if __name__ == '__main__':
    barrier = threading.Barrier(2)
    t1 = threading.Thread(target=work1, args=(barrier,))
    t2 = threading.Thread(target=work2, args=(barrier,))
    t1.start()
    t2.start()

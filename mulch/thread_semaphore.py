import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def work1(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')


def work2(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')


def work3(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')


if __name__ == '__main__':
    d = {'x': 0}
    # 指定した数（2つ）だけ動作させる
    semaphore = threading.Semaphore(2)
    t1 = threading.Thread(target=work1, args=(semaphore, ))
    t2 = threading.Thread(target=work2, args=(semaphore, ))
    t3 = threading.Thread(target=work3, args=(semaphore, ))
    t1.start()
    t2.start()
    t3.start()

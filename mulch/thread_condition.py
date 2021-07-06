import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def work1(condition):
    with condition:
        # conditionで処理を中断
        condition.wait()
        logging.debug('中断したwork1 start')
        time.sleep(2)
        logging.debug('work1 end after work3end 2sec wait')


def work2(condition):
    with condition:
        condition.wait()
        logging.debug('中断したwork2 start')
        time.sleep(4)
        logging.debug('work2 end after work3end 4sec wait')


def work3(condition):
    with condition:
        logging.debug('work3 start')
        time.sleep(2)
        logging.debug('work3 end after 2sec wait')
        # conditionで中断した処理を再開
        condition.notifyAll()


if __name__ == '__main__':
    condition = threading.Condition()
    t1 = threading.Thread(target=work1, args=(condition,))
    t2 = threading.Thread(target=work2, args=(condition,))
    t3 = threading.Thread(target=work3, args=(condition,))
    t1.start()
    t2.start()
    t3.start()

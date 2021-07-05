import logging
import queue
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def work1(queue):
    logging.debug('start')
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()
    # queue.put(100)
    # time.sleep(5)
    # queue.put(200)
    logging.debug('Looooooooooooong')
    logging.debug('end')


def work2(queue):
    logging.debug('start')
    time.sleep(5)
    # スレッド間でデータをやりとりできる
    print(queue.get())
    # 値が出るまで待つ
    print(queue.get())
    logging.debug('end')


if __name__ == '__main__':
    queue = queue.Queue()
    # 大量の処理を実行
    for i in range(10000):
        queue.put(i)
    # 3つに分けて処理
    ts = []
    for _ in range(3):
        t = threading.Thread(target=work1, args=(queue, ))
        t.start()
        ts.append(t)

    # t2 = threading.Thread(target=work2, args=(queue, ))
    logging.debug('tasks are not done')
    # t2.start()
    queue.join()
    logging.debug('tasks are done')

    # スレッド数終了処理
    for _ in range(len(ts)):
        queue.put(None)

    [t.join() for t in ts]
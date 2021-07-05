import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def work1(d, lock):
    logging.debug('start')
    # withでまとめると終了時にreleaseを実行
    with lock:
        i = d['x']
        time.sleep(5)
        d['x'] = i + 1
        logging.debug(d)
        with lock:
            # RLockでない場合、実行できずプログラムが止まらなくなる
            d['x'] = i + 1
    logging.debug('end')


def work2(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')


if __name__ == '__main__':
    # # enumerateスレッドの内容を返すので配列を使って表示する必要がない
    # # threads = []
    # for _ in range(5):
    #     # Timerで2秒後に実行
    #     t = threading.Timer(2, work1)
    #     t.setDaemon(True)
    #     t.start()
    #     # 準備した配列に収める（不要）
    #     # threads.append(t)
    # print(threading.enumerate())
    #
    # for thread in threading.enumerate():
    #     # mainを抜く
    #     if thread is threading.currentThread():
    #         print(thread)
    #         continue
    #     thread.join()

    # print('ALL COMPLETE')

    # t1 = threading.Thread(target=work1)
    # # デーモン化で裏で動作させる
    # t1.setDaemon(True)
    # t2 = threading.Thread(target=work2)
    # t1.start()
    # t2.start()
    # # 完結するまで待つ
    # t1.join()
    # print('ALL COMPLETE')
    d = {'x': 0}
    # RLockはreleaseされていないコード内でlockが使える
    lock = threading.RLock()
    t1 = threading.Thread(target=work1, args=(d, lock))
    t2 = threading.Thread(target=work2, args=(d, lock))
    t1.start()
    t2.start()

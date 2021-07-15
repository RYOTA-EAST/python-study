import asyncio

loop = asyncio.get_event_loop()


async def worker1(lock):
    print('worker1 start')
    # lockを先に取得した方が実行
    with await lock:
        print('worker1 lock')
        await asyncio.sleep(3)
    print('worker1 end')

async def worker2(lock):
    print('worker2 start')
    with await lock:
        print('worker2 lock')
        await asyncio.sleep(3)
    print('worker2 end')

lock = asyncio.Lock()
loop.run_until_complete(asyncio.wait(
    [worker1(lock), worker2(lock)]
))
loop.close()
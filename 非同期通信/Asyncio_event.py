import asyncio
import asyncio

loop = asyncio.get_event_loop()


async def worker1(event):
    print('worker1 start')
    # lockを先に取得した方が実行
    await event.wait()
    print('worker1 got event')
    await asyncio.sleep(3)
    print('worker1 end')

async def worker2(event):
    print('worker2 start')
    await event.wait()
    print('worker2 got event')
    await asyncio.sleep(3)
    print('worker2 end')

async def worker3(event):
    print('worker3 start')
    await asyncio.sleep(3)
    print('worker3 end')
    # 終了してから1と2を実行
    event.set()


event = asyncio.Event()
loop.run_until_complete(asyncio.wait(
    [worker1(event), worker2(event), worker3(event)]
))
loop.close()
import asyncio
from time import sleep, strftime
from concurrent import futures


def blocked(t):
    print(strftime('[%H:%M:%S]'), end=' ')
    print('{} sleep:{}s....'.format(t, t))
    sleep(t)
    print(strftime('[%H:%M:%S]'), end=' ')
    print('{} finished'.format(t))
    return t


@asyncio.coroutine
def main():
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        loop = asyncio.get_event_loop()
        future = [loop.run_in_executor(executor, blocked, i) for i in range(1, 7)]
        fs = asyncio.as_completed(future)
        results = []
        for f in fs:
            result = yield from f
            print('result:', result)
            results.append(result)
        return results


loop = asyncio.get_event_loop()
results = loop.run_until_complete(main())
print('results: {}'.format(results))
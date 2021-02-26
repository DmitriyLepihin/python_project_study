import asyncio
import os
import glob
from itertools import islice
import functools
import time
from contextlib import contextmanager


def clear_photos_directory():
    files = glob.glob('photos/*')
    for f in files:
        os.remove(f)


def timing_corutine(func):
    @contextmanager
    def wrapping_logic():
        start_ts = time.time()
        yield
        dur = time.time() - start_ts
        print('{} took {} seconds'.format(func.__name__, dur))

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not asyncio.iscoroutinefunction(func):
            with wrapping_logic():
                return func(*args, **kwargs)
        else:
            async def tmp():
                with wrapping_logic():
                    return await func(*args, **kwargs)

            return tmp()

    return wrapper


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} s'.format(f.__name__, (time2 - time1)))
        return ret

    return wrap


def chunks(data, SIZE=10000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}


def chunk_dict(urls):
    chunked_urls = []
    for item in chunks({i: urls.image_urls[str(i)] for i in range(100)}, 25):
        chunked_urls.append(item)
    return chunked_urls

import asyncio
import os
import random
import concurrent.futures

import aiofiles
import aiohttp
import requests
from multiprocessing import Pool, cpu_count
from functools import partial
import os
import asyncio
import functools
import time
from contextlib import contextmanager
import aiohttp
import aiofiles
from mp_pr import urls
from mp_pr.utils import clear_photos_directory, timing, chunks, timing_corutine

clear_photos_directory()


@timing_corutine
def download_images(ch_urls):
    sema = asyncio.BoundedSemaphore(100)

    async def download_image(num, url):
        async with sema, aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                # assert resp.status == 200
                data = await resp.read()

        async with aiofiles.open(
                os.path.join('photos', f'image_{num}.jpg'), "wb"
        ) as outfile:
            await outfile.write(data)

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(download_image(num, url)) for num, url in ch_urls.items()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


def start():
    pool = Pool(cpu_count())
    chunked_urls = []
    for item in chunks({i: urls.image_urls[str(i)] for i in range(100)}, 25):
        chunked_urls.append(item)
    results = pool.map(download_images, chunked_urls)
    pool.close()
    pool.join()


start()

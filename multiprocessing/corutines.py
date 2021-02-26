import os
import asyncio

import aiohttp
import aiofiles

from multiprocessing import urls
from multiprocessing.utils import clear_photos_directory, timing_corutine

clear_photos_directory()


@timing_corutine
def download_images():
    sema = asyncio.BoundedSemaphore(100)

    async def download_image(num, url):
        async with sema, aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.read()

        async with aiofiles.open(
                os.path.join('photos', f'image_{num}.jpg'), "wb"
        ) as outfile:
            await outfile.write(data)

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(download_image(num, url)) for num, url in urls.image_urls.items()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


download_images()

import concurrent.futures
import requests
from multiprocessing import Pool, cpu_count
from mp_pr.utils import chunks

from mp_pr import urls
from mp_pr.utils import clear_photos_directory, timing

clear_photos_directory()


def download_image(num, url):
    img_data = requests.get(url).content
    with open(f'photos/image_{num}.jpg', 'wb') as handler:
        handler.write(img_data)


def download_images(ch_urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for num, url in ch_urls.items():
            executor.submit(download_image, num, url)


@timing
def start():
    pool = Pool(cpu_count())
    chunked_urls = []
    for item in chunks({i: urls.image_urls[str(i)] for i in range(100)}, 25):
        chunked_urls.append(item)
    results = pool.map(download_images, chunked_urls)
    # pool.close(pool)
    # pool.join()


start()

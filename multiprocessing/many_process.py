import requests
from multiprocessing import Pool, cpu_count
from functools import partial

from multiprocessing import urls
from multiprocessing.utils import clear_photos_directory, timing

clear_photos_directory()


def download_image(url_obj):
    num, url = url_obj
    img_data = requests.get(url).content
    with open(f'photos/image_{num}.jpg', 'wb') as handler:
        handler.write(img_data)


@timing
def download_images():
    pool = Pool(cpu_count())
    download_func = partial(download_image)
    results = pool.map(download_func, urls.image_urls.items())
    pool.close()
    pool.join()


if __name__ == '__main__':
    download_images()

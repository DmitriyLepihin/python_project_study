import requests
import concurrent.futures

from multiprocessing import urls
from multiprocessing.utils import timing, clear_photos_directory

clear_photos_directory()


def download_image(num, url):
    img_data = requests.get(url).content
    with open(f'photos/image_{num}.jpg', 'wb') as handler:
        handler.write(img_data)


@timing
def download_images():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for num, url in urls.image_urls.items():
            executor.submit(download_image, num, url)


download_images()

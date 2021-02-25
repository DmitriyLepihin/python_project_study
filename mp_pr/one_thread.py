import requests

from mp_pr import urls
from mp_pr.utils import clear_photos_directory, timing

clear_photos_directory()


@timing
def download_images():
    for num, url in urls.image_urls.items():
        img_data = requests.get(url).content
        with open(f'photos/image_{num}.jpg', 'wb') as handler:
            handler.write(img_data)


download_images()

import requests
import time
from datetime import timedelta

my_urls = []
for url in range(1, 128):
    if url == 124 or url == 125 or url == 126:
        url = str(url)
        my_urls.append(f"https://golangshow.com/cdn/episodes/{url}-en.mp3")
        continue
    if url == 123:
        my_urls.append(f"https://golangshow.com/cdn/episodes/123-ru.mp3")
        my_urls.append(f"https://golangshow.com/cdn/episodes/123-en.mp3")
        continue
    if url == 127:
        my_urls.append(f"https://golangshow.com/cdn/episodes/127-en-draft.mp3")
        continue
    if url == 29:
        my_urls.append(f"https://golangshow.com/cdn/episodes/interview_bred.mp3")
        continue
    if url == 30:
        my_urls.append(f"https://golangshow.com/cdn/episodes/interview_rob.mp3")
        continue
    else:
        url = str(url)
        my_urls.append(f"https://golangshow.com/cdn/episodes/{url.zfill(3)}.mp3")


def code_time(func):
    def final(urls):
        start = time.time()
        func(urls)
        finish = time.time()
        print(f"{timedelta(seconds=finish - start)}")

    return final


@code_time
def download_mp3(urls):
    for url_address in urls:
        req = requests.get(url_address, stream=True)
        if req.status_code == requests.codes.ok:
            with open(f"D:\\golangshow\\golangshow{urls.index(url_address)}.mp3", 'wb') as f:
                f.write(req.content)
        else:
            print(f"Not connection url {url_address}")


download_mp3(my_urls)

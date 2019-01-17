import re
import os
import requests
from celery import Celery
from bs4 import BeautifulSoup

from settings import STORAGE_DIR

celery_app = Celery('tasks', backend='amqp', broker='amqp://localhost')

@celery_app.task
def get_text(site):
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')

    for script in soup(["script", "style"]):
        script.extract()

    raw_text = soup.get_text()
    lines = [line for line in raw_text.splitlines() if line]

    directory = STORAGE_DIR + os.path.basename(site) + '/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(directory + 'content.txt', 'w') as f:
        f.writelines(lines)


@celery_app.task
def get_images(site):
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]

    directory = STORAGE_DIR + os.path.basename(site) + '/img/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    for url in urls:
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
        if filename:
            with open(directory + filename.group(1), 'wb') as f:
                if 'http' not in url:
                    url = '{}{}'.format(site, url)
                response = requests.get(url)
                f.write(response.content)

import requests
from bs4 import BeautifulSoup
import urllib
from pathlib import Path
import time


def getImageUrl(load_url):
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, 'html.parser')

    separatorImgSrc = soup.find(class_='separator').find('img').get('src')
    print('imageUrl =' + separatorImgSrc)
    return separatorImgSrc


getImageUrl(input())

import requests
from bs4 import BeautifulSoup
import urllib
from pathlib import Path
import time


def createSoup(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    return soup


def hasNextButton(parameter_list):
    """
    docstring
    """
    pass


def getImageUrl(url):
    soup = createSoup(url)
    separatorImgSrc = soup.find(class_='separator').find('img').get('src')

    if separatorImgSrc[0:6] != 'https:':
        separatorImgSrc = 'https:' + separatorImgSrc

    return separatorImgSrc


def downloadImage(imageUrl):

    out_folder = Path('download6')
    out_folder.mkdir(exist_ok=True)

    imgdata = requests.get(imageUrl)

    filename = imageUrl.split('/')[-1]
    out_path = out_folder.joinpath(filename)

    with open(out_path, mode='wb') as f:
        f.write(imgdata.content)
        pass


def readResultHtml(keyword, index):
    step = 5
    start = step * index
    baseUrl = f"https://www.irasutoya.com/search?q={keyword}&max-results={step}&start={start}&by-date=false"

    soup = createSoup(baseUrl)

    urlList = []
    for element in soup.find_all(class_='post-outer'):
        readUrl = element.find(class_='boxim').find('a').get('href')

        urlList.append(readUrl)

        time.sleep(1)

    return urlList


keyword = 'ラーメン'

for i in range(2):
    uriList = readResultHtml(urllib.parse.quote(keyword), i)

    for url in uriList:
        imageUrl = getImageUrl(url)

        downloadImage(imageUrl)

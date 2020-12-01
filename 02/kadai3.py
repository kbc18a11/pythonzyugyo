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


def downloadImage(imageUrl):

    out_folder = Path('download4')
    out_folder.mkdir(exist_ok=True)

    imgdata = requests.get(imageUrl)

    filename = imageUrl.split('/')[-1]
    out_path = out_folder.joinpath(filename)

    with open(out_path, mode='wb') as f:
        f.write(imgdata.content)
        pass


imageUrl = getImageUrl('https://www.irasutoya.com/2017/10/blog-post_791.html')
downloadImage(imageUrl)

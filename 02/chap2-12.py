import requests
from bs4 import BeautifulSoup
import urllib


# Webページを取得して解析する
load_url = "https://ranking.goo.ne.jp/select/4039#headline_5253518"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")


for element in soup.find_all(class_='imageFromUrl active'):
    src = element.get('src')

    image_url = urllib.parse.urljoin(load_url, src)
    filename = image_url.split('/')[-1]
    print(f"{image_url} >> {filename}")

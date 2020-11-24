import requests
from bs4 import BeautifulSoup
import urllib
from pathlib import Path
import time

# Webページを取得して解析する
load_url = 'https://ranking.goo.ne.jp/select/4039#headline_5253518'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

out_folder = Path('download3')
out_folder.mkdir(exist_ok=True)

cnt = 0
for element in soup.find_all(class_='imageFromUrl active'):
    cnt += 1
    src = element.get('src')

    image_url = urllib.parse.urljoin(load_url, src)
    imgdata = requests.get(image_url)

    filename = image_url.split('/')[-1][0:13]
    out_path = out_folder.joinpath(filename)

    with open(out_path, mode='wb') as f:
        f.write(imgdata.content)

    print(f"{cnt}枚名完了")
    time.sleep(1)

print(f"合計{cnt}枚")

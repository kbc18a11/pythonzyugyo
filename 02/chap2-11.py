import requests
from pathlib import Path

out_folder = Path("download")
out_folder.mkdir(exist_ok=True)

# Webページを取得して解析する
load_img = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(load_img)

filename = load_img.split('/')[-1]
out_path = out_folder.joinpath(filename)

with open(out_path, mode='wb') as f:
    f.write(imgdata.content)

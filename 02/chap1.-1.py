import requests

url = "http://www.livedoor.com/"

res = requests.get(url)

res.encoding = res.apparent_encoding

fname = "a.txt"
with open(fname, mode="w") as f:
    f.write(res.text)
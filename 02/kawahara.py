import requests
from bs4 import BeautifulSoup

load_url = "https://kbc.kawahara.ac.jp/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

chap2 = soup.find(class_="line2-list")
for element in chap2.find_all("li"):
    print(element.text)
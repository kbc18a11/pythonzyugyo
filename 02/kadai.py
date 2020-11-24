import requests
from bs4 import BeautifulSoup

url = "https://paiza.jp/student/search?c%5Bnew_graduates_target_year%5D=2022&recommend=true"

res = requests.get(url)

soup = BeautifulSoup(res.content, "html.parser")

offerBox = soup.find(class_="boxPickup")

for element in offerBox.find_all(class_="c-job_offer-box"):
    print(element.find(class_="c-job_offer-recruiter__name").text)
    print(element.find(class_="c-job_offer-detail__occupation").text)

    try:
        print(element.find(class_="c-job_offer-detail__salary").text)
    except AttributeError:
        print("給料が存在しません")

    print("\n")

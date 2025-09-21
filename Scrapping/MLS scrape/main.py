import requests
from bs4 import BeautifulSoup
main_url = "https://scwmls.paragonrels.com/ParagonLS/Default.mvc/Login"
u2 = "https://scwmls.paragonrels.com/ParagonLS/Home/Page.mvc/MarketMonitorSubmit?daysBack=1&category=4&sectionType=Market&useInferno=true&searchID=tab1_1"

payload = {
    "LoginName" : "Juraj Janos",
    "Password" : "Jurko123"
}

p2 = {
    "LoginName" : "Juraj Janos",
    "Password" : "Jurko123",
    "MLSID": "SCWMLS"
}

p3= {
    "daysBack": "1",
    "category": "4",
    "sectionType": "Market",
    "useInferno": "true",
    "searchID": "tab1_1"
}

with requests.Session() as s:
    s.post(main_url, data = payload)
    s.post(main_url, data=p2)
    r = s.get(u2, data=p3)
    with open('file_name.txt', 'xb') as f:
        f.write(r.content)
    soup = BeautifulSoup(r.content, "html.parser")
    print(soup.prettify())
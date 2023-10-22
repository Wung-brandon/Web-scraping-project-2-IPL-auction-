import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.iplt20.com/stats/2023"
r = requests.get(url)
#print(r.status_code)
soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_="st-table statsTable ng-scope")
#print(table)

tr = soup.find_all("tr", class_="st-table__head")
print(tr)
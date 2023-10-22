import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

table = soup.find("table", class_="ih-td-tab auction-tbl")
#print(table)

headers = table.find_all("th")
#print(headers)
column_head = []
for i in headers:
    names = i.text
    column_head.append(names)
#print(column_head)
df = pd.DataFrame(columns=column_head)
#print(df)
row = table.find_all("tr")[1:]
for i in row:
    data = i.find_all("td")
    row_data = [tr.text.strip() for tr in data]
    #print(row_data)
    l = len(df)
    df.loc[l] = row_data
    
print(df)
#print(row)
df.to_csv("IPL_auction_stats_2022.csv", index=False)

    
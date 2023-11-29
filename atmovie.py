import requests
from bs4 import BeautifulSoup
url = "http://www.atmovies.com.tw/movie/next/"
Data = requests.get(url)
Data.encoding = "utf-8"

sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".filmListAllX li")

for x in result:
  print("片名：" + x.find("img").get("alt"))
  print("介紹：http://www.atmovies.com.tw" + x.find("a").get("href"))
  print("海報：" + x.find("img").get("src").replace(" ", ""))

  t = x.find(class_="runtime").text
  print("上映：" + t[5:15])
  
  if "片長" in t:
    t1 = t.find("片長")
    t2 = t.find("分")
    print(t[t1:t2+1])
  else:
    print("目前尚無片長資訊")

  r = x.find(class_="runtime").find("img")
  if r == None:
    print("目前尚無分級資訊")
  else:
    print("分級：http://www.atmovies.com.tw/" + r.get("src"))

  print()

print(sp.find(class_="smaller09").text)
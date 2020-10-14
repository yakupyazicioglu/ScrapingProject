import requests
from bs4 import BeautifulSoup

headers_param = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
glassdoor= requests.get("https://www.idefix.com/yazarlar#/page=1",headers=headers_param)

jobs= glassdoor.content

soup=BeautifulSoup(jobs,"html.parser")

allJobs=soup.find_all('ul',{"class":"authors-list"})

for ul in allJobs:
    print(ul.find('a')['href'])

""" for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href']) """

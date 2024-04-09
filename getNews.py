import requests
from bs4 import BeautifulSoup
import json

class New:
  def __init__(self, _title, _age):
    self.title = _title
    self.age = _age

api = 'https://baomoi.com/tag/LITE.epi'
row = requests.get(api)
soup = BeautifulSoup(row.text, 'html.parser')
news = []
def getNew(): 
  myDiv = soup.find_all('h3', {"class": "font-semibold block"})
  for new in myDiv:
    newObject = New(new.a.get('title'), new.a.get('href'))
    news.append(newObject.__dict__)

getNew()
with open('output.json', 'w') as fileHandle:
    json.dump(news, fileHandle)
# print(soup.prettify())
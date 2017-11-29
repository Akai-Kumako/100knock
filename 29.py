#29.国旗画像のURLを取得する

import json
import re
import urllib.parse, urllib.request

with open("jawiki-country.json", "r") as f:
  for i in f:
    a = json.loads(i) 
    if a.get("title") == "イギリス":
      b = a.get("text").replace("<br/>\n", "").split("\n")

info = {}
regex = re.compile(u"^\|(.*?)\s*=\s*(.*?)$")
emph = re.compile("'{2,5}")
intl = re.compile(r"\[\[((.+?)\|)?(.+?)\]\]")
tag = re.compile(r"<\/?[ref|br][^>]*?>")
extl = re.compile(r"\[http:\/\/[^\]]*?\]")

def remove(text):
  text = emph.sub("", text)
  prov = intl.search(text)
  if prov != None:
    text = prov.group(3)
  text = tag.sub("", text)
  text = extl.sub("", text)
  
  return text

for j in b:
  c = regex.search(j)
  if c != None:
    info[c.group(1)] = remove(c.group(2))
  if j == "}}": break

img = info['国旗画像']

url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(img) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

request = urllib.request.Request(url)
connection = urllib.request.urlopen(request)

data = json.loads(connection.read().decode())

url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
print(url)

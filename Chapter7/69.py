#69. Webアプリケーションの作成
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo import DESCENDING
from string import Template

client = MongoClient('localhost', 27017)
db = client.kyoko
co = db.nlp_collection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    search = request.form['search']
    dive = []
    trap = {}
    results = {}
    dive.append({"$or": [{"name": search},
                         {"aliases.name": search},
                         {"tags.value": search}]})
    for div in dive:
      trap = {"$and": [trap, div]}
    data = co.find(trap)
    sort = data.sort("rating.count", DESCENDING)
    for v in sort:
      results[v.get("id")] = v
    
    contents = []
    total = len(results)
    for i, (k, z) in enumerate(results.items(), start=1):
      dict_template = {}
      dict_template["index"] = i
      dict_template["total"] = total
      dict_template["name"] = z.get("name")
      dict_template["id"] = z.get("id")
      if "aliases" in z:
        dict_template["aliases"] = ", ".join(
          [name["name"] for name in z.get("aliases")])
      else:
        dict_template["aliases"] = "該当なし"
      if "tags" in z:
        dict_template["tags"] = ", ".join(
          [tag["value"] for tag in z.get("tags")])
      else:
        dict_template["tags"] = "該当なし"
      dict_template["area"] = z.get("area")
      contents.append(dict_template)
      print(dict_template)
    return render_template('hello.html', search=search, contents=contents)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

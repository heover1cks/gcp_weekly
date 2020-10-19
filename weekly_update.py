from flask import Flask, jsonify
from flask_pymongo import PyMongo
from bs4 import BeautifulSoup as bs
import feedparser as fp

app = Flask(__name__)
app.config["MONGO_URI"] = ""
mongo = PyMongo(app)

gcp = fp.parse('https://cloud.google.com/feeds/gcp-release-notes.xml')
az = fp.parse('https://azurecomcdn.azureedge.net/ko-kr/updates/feed/')
aws = fp.parse('https://aws.amazon.com/ko/about-aws/whats-new/recent/feed/')
#print(gcp.entries[2].content[0].get('value'))



@app.route('/gcp')
def gcp_test():
    cur = gcp.entries[4].content[0].get('value')
    soup = bs(cur, 'lxml')
    ret = ""
    for idx in soup.find_all('strong', class_="release-note-product-title"):
        temp= idx.text + "<br>"
        ret += temp
        print(idx.find('p'))
    print(cur)
    return cur


@app.route('/gcp/dates')
def gcp_dates():
    ret = ""
    for i in range(len(gcp.entries)):
        ret += gcp.entries[i].title
        ret += "<br>"
    return ret

print(gcp.entries[4].content)
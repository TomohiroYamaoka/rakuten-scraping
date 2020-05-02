from flask import Flask
import requests
from bs4 import BeautifulSoup

app=Flask("Rakutenapp")


@app.route("/")
@app.route("/")
def myapp()

address = "https://review.rakuten.co.jp/item/1/203555_10001672/1.1/"
resp=requests.get(address)
data=resp.text
soup=BeautifulSoup(data,'lxml')






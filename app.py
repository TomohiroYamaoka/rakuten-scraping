from flask import Flask, url_for, render_template,flash
from bs4 import BeautifulSoup
#外部のサイトにアクセスすることができるモジュール
import requests
#エクセルファイルをしようすることができるモジュール
from openpyxl import Workbook 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("top.html")

@app.route("/", methods=["GET","POST"])
def rakuten_get(): 
    if request.form["rakuten.put"]:
        result=fetch()
        return render_template("")
    #楽天のwebページを取得する。
    r = request.get("https://review.rakuten.co.jp/item/1/203555_10001672/1.1/")
    #resp=requests.get(address)
    soup=BeautifulSoup(r.content,'html.parser')
    #各項目のHTMLを取得する、
    #購入者
    contentA=soup.select_one('#〇〇>div.▲▲>div.××').get_text(strip=True)
    #星の数
    contentB=soup.select_one('#〇〇>div.▲▲>div.××').get_text(strip=True)
    #商品の使い道
    contentC=soup.select_one('#〇〇>div.▲▲>div.××').get_text(strip=True)
    #商品を使う人
    contentD=soup.select_one('#〇〇>div.▲▲>div.××').get_text(strip=True)
    #購入した回数
    contentE=soup.select_one('#〇〇>div.▲▲>div.××').get_text(strip=True)
    #日付
    contentF=soup.select_one('#〇〇>div.▲▲>div.××').get_text(strip=True)
    #タイトル
    contentG=soup.select_one('#〇〇>div.▲▲>div.××').get_text(strip=True)
    #本文
    contentH=soup.select_one('#〇〇>div.▲▲>div.××').get_text(strip=True)
    
    
def fetch():
    wb=Workbook()
    ws=wb.activate
    ws.title='Sample'
    ws['A1'].value='購入者名'
    ws['B1'].value='星の数'
    ws['C1'].value='商品の使い道'
    ws['D1'].value='商品を使う人'
    ws['E1'].value='購入した回数'
    ws['F1'].value='日付'
    ws['G1'].value='タイトル'
    ws['H1'].value='本文'
    #取得したデータをループさせて、「data」に代入
    # for i in range()
    
    #値を出力する。
    makeData()
    
    #Excelにデータを保存する。
    wb.save('data.xlsx')

    if __name__ == '__main__':
        app.run(debug=True)
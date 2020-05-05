from flask import Flask, url_for, render_template,flash,request, redirect
from bs4 import BeautifulSoup
#外部のサイトにアクセスすることができるモジュール
import requests,bs4
import os
#エクセルファイルをしようすることができるモジュール
from openpyxl import Workbook 

app = Flask(__name__)

#ページを開いた時に処理をするところ。
@app.route("/", methods=["GET"])
def index():
    return render_template("top.html")


@app.route("/input", methods=["GET","POST"])
def input(): 
    if request.form["inputText"]:
        #def fetch（）の処理を実行し、「result」に代入する。
        result=fetch()

        #結果を「result.html」に表示させる。
        return render_template("result.html",data=result)

    else:
        flash("URLを入力してください。")
        return render_template("top.html")    


def fetch():
    #入力したURLをurl代入する。
    url=request.form["inputText"]
    #楽天のwebページを取得する。
    r = requests.get(url)
    #resp=requests.get(address)
    contenA=r.text

    """
    soup=BeautifulSoup(r.content,'html.parser')
    #各項目のHTMLを取得する、
    #購入者
    contentA=soup.select('revUseEntry >div.revRvwUserEntryCnt>dl.revRvwUserEntryInr > dd.revRvwUserEntryCmt description')
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
    """

    return contenA

    """
    wb=Workbook()
    ws=wb.activate

    #top.htmlでタイトルを出力させ、シート名になる
    ws.title='hoge'


    ws.title='Sample'
    ws['A1'].value='購入者名'
    ws['B1'].value='星の数'
    ws['C1'].value='商品の使い道'
    ws['D1'].value='商品を使う人'
    ws['E1'].value='購入した回数'
    ws['F1'].value='日付'
    ws['G1'].value='タイトル'
    ws['H1'].value='本文'
    
    #値を出力する。
    makeData()
    
    #saveでExcelファイルを保存する。
    wb.save('data.xlsx')
    """
if __name__ == '__main__':
    app.run(debug=True)
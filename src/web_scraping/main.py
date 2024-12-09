# seleniumの必要なライブラリをインポート
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from src.web_scraping.gspshi import SpreadSheet
import time
import datetime
import json
from icecream import ic
import tkinter
from tkinter import messagebox


def main():
    ##########################################
    # データスクレイピング
    ##########################################
    # 対話：処理開始を宣言
    print("PC site analysis start")

    ######## オプションを適宜設定
    options = Options()
    # 新しいヘッドレスモード指定
    # options.add_argument("--headless=new")

    ######### Googleアカウントのログイン状態に設定する(実施する場合はアンコメントすること)
    # appsetting = json.load(open("secrets_json/settings.json", "r"))
    # googleOAuthWinUserName = appsetting["googleOAuthWinUserName"]
    # googleOAuthProfileDir = appsetting["googleOAuthProfileDir"]
    ##### プロファイルのパスを通す
    # profilePath = r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(googleOAuthWinUserName)
    # options.add_argument(profilePath)
    ##### 使用するプロファイル(ユーザー)を指定
    # profileTargetUser = r"--profile-directory={}".format(googleOAuthProfileDir)
    # options.add_argument(profileTargetUser)

    # Chrome Webドライバー の インスタンスを生成
    driver = webdriver.Chrome(options=options)

    # サンプル：Yahooニュースの主要記事のタイトル
    res_yahoo = []
    URL = "https://news.yahoo.co.jp/"
    time.sleep(1)
    for i in range(8):
        xpath = '//*[@id="uamods-topics"]/div/div/div/ul/li[' + str(i + 1) + "]/a"
        driver.get(URL)
        elms = driver.find_element(By.XPATH, xpath)
        res_yahoo.append(elms.get_attribute("innerText"))

    ic(res_yahoo)

    # サンプル：日本経済新聞社サイトのアクセスランキングトップ１０記事タイトル
    res_nikkei = []
    URL = "https://www.nikkei.com/access/"
    time.sleep(1)
    for i in range(10):
        xpath = '//*[@id="CONTENTS_MAIN"]/div[1]/ul/li[' + str(i + 1) + "]/h3/span[2]/span[1]/a"
        driver.get(URL)
        elms = driver.find_element(By.XPATH, xpath)
        res_nikkei.append(elms.get_attribute("innerText"))

    ic(res_nikkei)

    ##########################################
    # スプレッドシート書き込み
    ##########################################
    ####インスタンスの生成
    sp = SpreadSheet()
    sp.addColsFromLeft(1, 3)
    sp.updateOneCell("A2", "追加日時")
    dt_now = datetime.datetime.now()
    sp.updateOneCell("B2", dt_now.strftime("%Y年%m月%d日 %H:%M:%S"))
    ####データの書き込み（ヤフー分）
    sp.updateOneCell("A3", "yahoo")
    sp.updateCellsVertical("A", 4, 11, res_yahoo)
    ####データの書き込み（日経分）
    sp.updateOneCell("B3", "nikkei")
    sp.updateCellsVertical("B", 4, 13, res_nikkei)

    # データ収集完了を表示
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("selenium sapmle", "データ収集、完了！")

    # Webドライバー の セッションを終了
    driver.quit()


if __name__ == "__main__":
    main()

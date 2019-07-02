# coding: UTF-8
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':

    # URL関連
    top_url = "https://www.yahoo.co.jp/"
    url = "https://news.yahoo.co.jp/"

    # ヘッドレスモードを設定
    options = Options()
    options.add_argument('--headless')

    # Chromeを起動
    driver = webdriver.Chrome(options=options)

    # 一度トップページに行きCookieを取得
    driver.get(top_url)
    driver.get_cookies()
    driver.get(url)

    # soupオブジェクトを作成
    soup = BeautifulSoup(driver.page_source, "lxml")

    # タイトルリストを取得して表示
    for title in soup.find_all("dt", class_="titl"):
        print(title.get_text())

   # Chromeドライバーを終了 closeだとプロセスが残って終わってからも操作できない
    driver.quit()

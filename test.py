import time
import traceback
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
# ヘッドレスモードで実行する場合
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://keywordtool.io/search/keywords/amazon/3079379?category=aps&keyword=パソコン&country=JP&language=ja_JP#suggestions")
    # 簡易的にJSが評価されるまで秒数で待つ
    time.sleep(5)

    # セレクトボタンを押した後コピーボタンを押してコピーする
    select_button = driver.find_element_by_xpath('//*[@id="edit-operations-wrapper--5"]/div/button')
    select_button.click()
    copy_button = driver.find_element_by_xpath('//*[@id="edit-copy--5"]')
    copy_button.click()
    print(pyperclip.paste())
except:
    traceback.print_exc()
finally:
    driver.quit()

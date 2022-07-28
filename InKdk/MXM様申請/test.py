# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:36:32 2022

@author: 406429
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_path="chromedriver.exe"

driver = webdriver.Chrome(driver_path)
"""
# 起動時にオプションをつける。（ポート指定により、起動済みのブラウザのドライバーを取得）
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(executable_path=driver_path, options=options)


# ページのタイトルを表示する
print(driver.title)
print("========== source ========== ")
print(driver.page_source)
"""
#URLを読み込みます
google_url = 'https://www.google.com/' 
driver.get(google_url)
title = driver.title
#ここで、検索ボックスと検索ボタンを見つけます。
#NAMEの見つけ方はhttps://self-methods.com/selenium-howtouse/#index_id0 ここから
search_box = driver.find_element(By.NAME, 'q')
search_button = driver.find_element(By.NAME,"btnK")

#検索をします。
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)
#search_button.click()

#value = search_box.get_attribute("value")
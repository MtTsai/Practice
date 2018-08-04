#!/usr/bin/env python3

# For chinese
# -*- coding: UTF-8 -*-

# PhantomJs has been deprecated by Selenium support
#
# from selenium import webdriver
# 
# driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-windows/bin/phantomjs') # PhantomJs
# driver.get('http://pala.tw/js-example/') 
# pageSource = driver.page_source  # Get web source code
# print(pageSource)
# 
# driver.close() # closing browser

from selenium import webdriver

option = webdriver.ChromeOptions()
# option.add_argument('headless')
# option.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
chrome_path = "/cygdrive/d/GitSpace/WebCrawler/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(chrome_path, chrome_options=option)
driver.get('http://pala.tw/class-id-example/') # another example: 'http://pala.tw/js-example/'
print('Open browser')
# print(driver.title)
# driver.find_element_by_id('kw').send_keys('testing')
pageSource = driver.page_source

driver.get('https://vimeo.com/channels/affinityphoto')
vimeoSource = driver.page_source 

driver.quit()


print("=" * 80)

from bs4 import BeautifulSoup


print(pageSource)
soup = BeautifulSoup(pageSource, "lxml")

tag = '.半糖'
for drink in soup.select(tag):
        print(drink.get_text())
print("=" * 80)

tag = 'p'
for drink in soup.select(tag):
        print(drink.get_text())
print("=" * 80)

tag = '#老闆'
for drink in soup.select(tag):
        print(drink.get_text())
print("=" * 80)

print()
soup = BeautifulSoup(vimeoSource, "lxml")

tag = '.title'
for drink in soup.select(tag):
        print(drink.get_text())
print("=" * 80)

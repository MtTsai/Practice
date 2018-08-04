#!/usr/bin/env python3

# For chinese
# -*- coding: UTF-8 -*-

import time
from selenium import webdriver
from bs4 import BeautifulSoup

# PhantomJs has been deprecated by Selenium support
#
# driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-windows/bin/phantomjs') # PhantomJs
# driver.get('http://pala.tw/js-example/') 
# pageSource = driver.page_source  # Get web source code
# print(pageSource)
# 
# driver.close() # closing browser

################################################################################
#    ChromeDriver                                                              #
################################################################################

option = webdriver.ChromeOptions()
chrome_path = "/cygdrive/d/GitSpace/WebCrawler/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(chrome_path, chrome_options=option)

url = 'http://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html'
driver.get(url)
time.sleep(1)


# for i in range(10):
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#     time.sleep(1)

pageSrc = driver.page_source 

driver.close()
# driver.quit()


print("=" * 80)

# print(pageSrc)

# soup = BeautifulSoup(pageSrc, 'lxml')

# result = soup.select('#resultStats')[0].get_text()
# print(soup.select('#resultStats'))
# print('蟲師', result)

print(len(pageSrc))

from selenium import webdriver
import time
import random

'''
需要获得与浏览器相匹配的driver
http://chromedriver.storage.googleapis.com/index.html
'''
browse = webdriver.Chrome('./chromedriver')
url = "https://www.weibo.com"
browse.get(url)
for i in range(0,2):
    browse.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(random.randint(5,9))

file = open('./data','wb')
print(browse.page_source)
file.write(str(browse.page_source).encode())

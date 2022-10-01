from time import sleep

from selenium import webdriver


browser = webdriver.Firefox()
#hiudusfg

browser.get('https://www.instagram.com/')


sleep(5)


browser.close()

# -*- coding: utf-8 -*-
from selenium import webdriver
import time

browser=webdriver.Firefox()
browser.get("https://www.reddit.com")
browser.execute_script("window.open()")
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get("https://www.youtube.com")
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get("https://python.org")
#browser.close()
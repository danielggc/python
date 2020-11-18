from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import random

url='https://b-ok.cc/book/841322/55519c'
google=webdriver.Firefox()  
google.get(url)
urlHref=google.page_source
urlHref2=BeautifulSoup(urlHref,'html.parser')
urlHref2=urlHref2.find_all(class_="btn btn-primary dlButton addDownloadedBook")
print(urlHref2)

#href="/dl/841322/4c7992"
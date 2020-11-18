
from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", 'HOST')
profile.set_preference("network.proxy.http_port", 31280)
profile.set_preference("network.proxy.ssl", 'HOST')
profile.set_preference("network.proxy.ssl_port", 31280)
driver = webdriver.Firefox(firefox_profile=profile)
driver.get("https://www.expressvpn.com/es/what-is-my-ip")
sleep(10)
driver.close()
PROXY = proxies[0].get_address()
webdriver.DesiredCapabilities.FIREFOX['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    
    "proxyType":"MANUAL",
    
}
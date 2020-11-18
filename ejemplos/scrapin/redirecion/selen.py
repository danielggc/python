from selenium import webdriver
from time import sleep
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.selenium.dev')

# click radio button
sleep(1)
python_button = driver.find_elements_by_xpath('//a[@href="/downloads"]')[0]
python_button.click()
sleep(2)
python_button = driver.find_elements_by_xpath('//a[@href="https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar"]')[0]
python_button.click()

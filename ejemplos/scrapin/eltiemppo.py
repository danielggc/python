import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
dias=soup.find(id='seven-day-forecast')
horas=dias.find_all(class_="tombstone-container")
print(horas)
import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html="""[<div style="overflow: hidden; zoom: 1; margin-top: 30px;">
<div class="bookDetailsBox">
<div class="bookProperty property_year">
<div class="property_label">Year:</div>
<div class="property_value">1920</div>
</div>
<div class="bookProperty property_publisher">
<div class="property_label">Publisher:</div>
<div class="property_value">Fleming H. Revell Co </div>
</div>
<div class="bookProperty property_language">
<div class="property_label">Language:</div>
<div class="property_value">english</div>
</div>
<div class="bookProperty property_pages">
<div class="property_label">Pages:</div>
<div class="property_value"><span title="Pages paperback">160</span></div>
</div>
<div class="bookProperty property__file">
<div class="property_label">File:</div>
<div class="property_value">EPUB, 158 KB</div>
</div></div> </div>]
"""
soup=BeautifulSoup(html,'html.parser')
datos=re.sub("<div class=",' ',str(soup))
datos=re.sub('</div',' ',datos)
datos=re.sub('div',' ',datos)
datos=re.sub('property_label',' ',datos)
datos=re.sub('property_value',' ',datos)
datos=re.sub('<',' ',datos)
datos=re.sub('"',' ',datos)
datos=re.sub('>',' ',datos)
i =re.split(';',datos)
print("\n\n\n\n\n\n")
datos=i[3]
datos=re.sub(']',' ',datos)
if re.search(' EPUB',datos):
    tipo=re.search('EPUB',datos)
    print(tipo.group())
   
print(datos)









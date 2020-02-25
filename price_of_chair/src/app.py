__author__ = 'reubin'

#practice with http requests as well as Beautiful Soup
import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-partners-penny-office-chair/p1193212")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price price--large"})

string_price = element.text.strip() #£99.00
price =  float(string_price[1:])

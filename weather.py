# for using this need to install beautifulsoup4
# so to install run it in terminal :: "pip install beautifulsoup4"


import urllib.request
from bs4 import BeautifulSoup

city = input("Enter your city: ")

try:
    url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, 'html.parser')
    forecast = soup.find('span', {'class': 'phrase'}).text
    print(forecast)
except Exception as e:
    print("An error occurred:", e)

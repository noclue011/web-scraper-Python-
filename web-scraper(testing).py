# This page is filled with test code and is not the actual web scraper

# Grabs content of webpage
import requests
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
page.content
# Parse the content of webpage
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Checks what the type is for each element in list
[type(item) for item in list(soup.children)]
# Select the HTML tag and its children
html = list(soup.children)[2]
# Dive into the body of the page
body = list(html.children)[3]
# Isolate the p tag
p = list(body.children)[1]
p.get_text()

# Grab all instances of the p tag
soup.find_all('p')[0].get_text()
# find first instance of the p tag
soup.find('p')

# Test to get classes and ids from html
page = requests.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
soup
# find all p tags with class outer-text
soup.find_all('p', class_='outer-text')
# Find any tags with class outer-text
soup.find_all(class_="outer-text")
# Find all elements with a specific id
soup.find_all(id="first")

# Searching with css selectors
soup.select("div p")
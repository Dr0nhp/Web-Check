from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

request_url = 'https://www.nytimes.com/'

uGrabPage = uReq(request_url)
page_html = uGrabPage.read()
uGrabPage.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs containers

#TODO Which Containers are interesting? 
container = page_soup.find_all("")


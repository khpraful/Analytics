import bs4 as bs
import urllib
import requests

htmlfile = urllib.urlopen("http://www.amazon.in/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=samsung+mobile")
htmltext = htmlfile.read()
soup = bs.BeautifulSoup(htmltext, 'lxml')
containers = soup.findAll("div", {"class":"s-item-container"})
print(len(containers))
container = containers[0]
print container



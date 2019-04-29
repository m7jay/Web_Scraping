
# coding: utf-8

# In[2]:


from urllib.request import urlopen
from urllib.error import HTTPError , URLError
from bs4 import BeautifulSoup
import datetime , random , re

random.seed(datetime.datetime.now())

pages=set()

def getlinks(url):
    try:
        html = urlopen(url)
    except HTTPError as h:
        print("Page not found")
    except URLError as u:
        print("URL not found")
    try:
        bs = BeautifulSoup(html)
        body_content = bs.find("div",{"id":"bodyContent"})
        links = body_content.findAll('a',href=re.compile("^(/wiki/)((?!:).)*$"))
    except AttributeError as a:
        print("Attribute not found eror")
    return links

links = getlinks("http://en.wikipedia.org/wiki/Kevin_Bacon")
#for l in links:
#    if 'href' in l.attrs:
#        print(l.attrs['href'])

while len(links)>200:
    newarticle = links[random.randint(0,len(links)-1)].attrs['href']
    if newarticle not in pages:
        print(newarticle)
        pages.add(newarticle)
    links = getlinks("http://en.wikipedia.org/" + newarticle)


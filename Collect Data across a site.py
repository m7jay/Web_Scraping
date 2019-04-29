
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from urllib.error import HTTPError , URLError
from bs4 import BeautifulSoup
import datetime , random , re

random.seed(datetime.datetime.now())

pages=set()


# In[2]:


def getlinks(url):
    global pages
    try:
        html = urlopen("http://en.wikipedia.org"+url)
    except HTTPError:
        print("Page not found")
    except URLError:
        print("URL not found")
    try:
        bs = BeautifulSoup(html)
        header=bs.h1
        print("Header:"+header.get_text())
        para=bs.find("div",{"id":"mw-content-text"}).findAll("p")[0]
        print("Paragraph:\n"+para.get_text())
        l=bs.find("li",{"id":"ca-edit"}).find("span").find("a").attrs["href"]
        print("Editable Link:\n"+l.get_text())
    except AttributeError:
        print("Attribute not found eror")
    for links in bs.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in links.attrs:
            if links.attrs['href'] not in pages:
                newpage = links.attrs['href']
                print("-------------------------------------------------------------------------------\n"+newpage)
                pages.add(newpage)
                getlinks(newpage)
                            


# In[3]:


getlinks("/wiki/Kevin_Bacon")



# coding: utf-8

# In[2]:


from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def Get_Title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return "Page not found"
    except URLError as u:
        return "URL not found"
    try:
        bs_obj = BeautifulSoup(html.read())
        title = bs_obj.script.sometag.anothertag
    except AttributeError as e:
        return "Attribute Not Found" 
    return title
    

title = Get_Title("http://www.google.com")
if title == None:
    print("None obj returned")
else:
    print(title)


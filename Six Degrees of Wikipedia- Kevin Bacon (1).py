
# coding: utf-8

# In[ ]:


from urllib.request import urlopen
from bs4 import BeautifulSoup , re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bs_obj = BeautifulSoup(html)

#links = bs_obj.findAll('a')
body_content = bs_obj.find("div",{"id":"bodyContent"})
links = body_content.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

for link in links :
    if 'href' in link.attrs:
        print(link.attrs['href'])


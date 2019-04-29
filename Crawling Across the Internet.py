
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from urllib.error import HTTPError , URLError
from bs4 import BeautifulSoup
import re , datetime , random

pages = set()
random.seed(datetime.datetime.now())


# In[2]:


#Retrieves all internal links found on a page
def GetInternalLinks(bsobj, includeurl):
    internalLinks = []
    for links in bsobj.findAll("a", href=re.compile("^(/|.*"+includeurl+")")):
        if links.attrs['href'] is not None:
            if links.attrs['href'] not in internalLinks:
                internalLinks.append(links.attrs['href'])
    return internalLinks
            


# In[3]:


#Retrieves a list of all external links
def GetExternalLinks(bsobj, excludeurl):
    externalLinks = []
    for links in bsobj.findAll("a", href=re.compile("^(http|www)((?!"+excludeurl+").)*$")):
        if links.attrs['href'] is not None:
            if links.attrs['href'] not in externalLinks:
                externalLinks.append(links.attrs['href'])
    return externalLinks


# In[4]:


def SplitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts


# In[5]:


def GetRandomExternalLink(StartingPage):
    try:
        html = urlopen(StartingPage)
    except HTTPError:
        print("Page not found")
    except URLError:
        print("URL not found")
    try:
        bsobj = BeautifulSoup(html)
    except AttributeError:
        print("Attribute not found")
    externalLinks = GetExternalLinks(bsobj, SplitAddress(StartingPage)[0])
    if len(externalLinks) == 0:
        print("\nNo external links found in "+StartingPage+"\nLooking in internal links to find any external links\n")
        internalLinks = GetInternalLinks(bsobj, StartingPage)
        return GetExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]
        


# In[6]:


def FollowExternalLinkOnly(StartingSite):
    externalSite = GetRandomExternalLink(StartingSite)
    print("Random External Link is:\n"+externalSite)
    FollowExternalLinkOnly(externalSite)

#FollowExternalLinkOnly("http://google.com")


# In[7]:


#Retrieve all external links
AllExternalLinks = set()
AllInternalLinks = set()
def GetAllExternalLinks(SiteUrl):
    try:
        html = urlopen(SiteUrl)
    except HTTPError:
        print("Page not found")
    except URLError:
        print("URL not found")
    try:
        bsobj = BeautifulSoup(html)
    except AttributeError:
        print("Attrbute not found")
    internalLinks = GetInternalLinks(bsobj, SplitAddress(SiteUrl)[0])
    externalLinks = GetExternalLinks(bsobj, SplitAddress(SiteUrl)[0])
    for link in externalLinks:
        if link not in AllExternalLinks:
            AllExternalLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in AllInternalLinks:
            AllInternalLinks.add(link)
            print("About to get link:"+link)
            GetAllExternalLinks(link)


# In[8]:


GetAllExternalLinks("https://oreilly.com/")


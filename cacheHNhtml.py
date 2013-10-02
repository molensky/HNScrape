from bs4 import BeautifulSoup
import urllib2

# save a series of HN pages for offline use
baseurl = "https://news.ycombinator.com"
page = "/item?id=6475879"
ext = "html"
pg = 1
while page != '':
    content = urllib2.urlopen(baseurl+page).read()
    soup = BeautifulSoup(content)
    
    name = "%s.%s" % (pg,ext)
    print baseurl+page,">>",name
    f = open(name, 'w')
    f.write(content)
    f.close()
    pg += 1
    
    # find the next link in the chain
    page = ''
    titles = soup.find_all(class_="title")
    for t in titles:
        if t.get_text() == "More":
            page = t.a.get('href')
            
    
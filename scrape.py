from bs4 import BeautifulSoup
import urllib2

baseurl = "https://news.ycombinator.com"
page = "/item?id=6475879"

while page != '':
    content = urllib2.urlopen(baseurl+page).read()
    soup = BeautifulSoup(content)

    #print soup.prettify().encode('utf-8')
    comments = soup.find_all("span", class_="comment")
    for comment in comments:
        #TODO do something more meaningful 
        print comment.get_text().encode('utf-8')
    
    # find the next link in the chain
    page = ''
    titles = soup.find_all(class_="title")
    for t in titles:
        if t.get_text() == "More":
            page = t.a.get('href')
            print baseurl+page
            
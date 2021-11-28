from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
url = "https://noveltrench.com/manga/page/350"

#saves the novel list into a text file
def save(list1):
    with open("novelList.txt","a", encoding="utf-8")as f:
        for i in list1:
            f.writelines(str(i) + "\n")

#scrapes novels
def scraping_novels(url):
    novel_links = []
    #using request-html instead of requests since it can scrape content added by javascript
    session = HTMLSession()

    rs = session.get(url)

    #renders the page for the javascript to finish adding content to the page
    rs.html.render(timeout=10)


    #yeah ignore this pile of shit basically error checking with an if statement
    if rs.status_code != 200:
        print("PAGE ENDS I GUESS STATUS CODE IS NOT 200")
        return int(404)


    #if the states code is 200 congrats
    if rs.status_code == 200:

        #so here we are finding all the links i guess good luck you can also extract the names pretty easily
        #by the way if you use regular expressions its easier
        soup = BeautifulSoup(rs.content,"html.parser")
        result = soup.find_all("div", attrs={"class":"page-listing-item"})


        for div in result:
            x = div.find_all('a')
            for r in x:
                if "chapter-" not in r["href"]:
                    print(r["href"])
                    if r["href"] not in novel_links:
                        novel_links.append(r["href"])
                        print(novel_links)

        return novel_links


def getting_novel_links():
    for i in range(1,500):
        # I guess you can understand this part
        list1 = scraping_novels("https://noveltrench.com/manga/page/{}".format(i))
        if list1 == int(404):
            break
        save(list1)



getting_novel_links()







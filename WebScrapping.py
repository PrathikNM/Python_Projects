import urllib.request as ur                                                          # importing urllib python library for url related operation

from bs4 import BeautifulSoup                                                        #importing beautifulsoup library for webscrapping


class Web_Scraping:
    def __init__(self, webpage):
        self.webpage = webpage

    def scraping(self):                                                              # creating object to extract required urls/links
        html_page = ur.urlopen(self.webpage)
        html_data = html_page.read()
        soup = BeautifulSoup(html_data,"html.parser")
        for tag in soup.find_all("a"):
            link = tag.get("href")
            if link is None:
                continue
            if "articles" in link:
                with open ('Webscraping_data.txt','a') as wd:                        # Writing extracted links into Webscraping_data text file 
                    wd.write(link)
                    wd.write("\n")
                    wd.close()
                

news_link = "https://news.google.com/"                                               #creating a constructor to call the scraping object inthe Web_scrapping class
task = Web_Scraping(news_link)
task.scraping()


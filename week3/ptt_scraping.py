import urllib.request,csv
from bs4 import BeautifulSoup 

class PTT():
    
    def __init__(self):
        self.TitleList = []
        self.LikeList = []
        self.TimeList= []
        self.html_parsed = ''

    def get_html(self,url):
        url = urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.82"})
        data = urllib.request.urlopen(url)
        html = data.read().decode("utf-8")
        self.html_parsed = BeautifulSoup(html, "html.parser")
        return self.html_parsed

    def page(self):

        page = self.html_parsed.find_all("a", class_="btn wide")
        next_page_url= "https://www.ptt.cc/" + page[1].get("href")
        return next_page_url

    def get_info(self):
        
        titles = self.html_parsed.find_all("div", class_="title")
        nums =  self.html_parsed.find_all("div", class_="nrec")
        
        for num in nums:
            try:
                get_span = num.find("span").getText()
                self.LikeList.append(get_span)
            except AttributeError:
                self.LikeList.append(0)

        for title in titles:
            try:
                Title = title.find("a").getText()
                self.TitleList.append(Title)
            except AttributeError:
                self.TitleList.append("已刪文")
                
            try:
                txt = title.find("a").get("href")
                site = "https://www.ptt.cc/" + txt
                html3 = self.get_html(site)
                time = html3.find_all("span", class_="article-meta-value")
                Time = time[3].getText()
                self.TimeList.append(Time)
            except AttributeError:
                self.TimeList.append("0")

    def wirte_In(self):
        with open('movie.csv', 'w',encoding='utf-8',newline='') as csv_f:
         writer = csv.writer(csv_f)
         for i in range(len(self.TimeList)):
             writer.writerow([self.TitleList[i],self.LikeList[i],self.TimeList[i]])
            
page_to_scrape = input("How many pages do you want? :")

P = PTT()
for i in range(int(page_to_scrape)):
    if i == 0:
        first_page = P.get_html("https://www.ptt.cc//bbs/movie/index.html")
        next = P.page()
        P.get_info()
        P.wirte_In()
        
    else:
        next_page = P.get_html(next)
        next = P.page()
        P.get_info()
        P.wirte_In()
        



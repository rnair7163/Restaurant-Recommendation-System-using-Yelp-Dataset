import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

base_url= 'https://www.tripadvisor.com/Restaurant_Review-g36806-d1674873-Reviews-Black_Dog_Smoke_Ale_House-Urbana_Champaign_Urbana_Illinois.html#REVIEWS'
base_search_url='https://www.tripadvisor.com'
urls=[]
urls.append(base_url)
reviews=[]


while len(urls)>0:
    for i in range(2,61):
        print(urls)
        url=urls.pop(0)
        uClient = uReq(url)
        page_html = uClient.read()
        page_soup = soup(page_html)
        entry = page_soup.findAll("div",{"class":"entry"})
        for entries in entry :
            reviews.append(entries.text)
        page = page_soup.findAll("div",{"class":"pageNumbers"})
        next_url =page[0].find("a",{"data-page-number":i})
        if next_url: # if it's not an empty string
            urls.append(base_search_url + next_url['href']) 
    
import pandas
pandas.DataFrame(reviews).to_csv('D:/CSP 571/yelp data/trip_advisor_trial_1.csv')
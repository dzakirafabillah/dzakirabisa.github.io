import requests
import json
import os
import datetime
from bs4 import BeautifulSoup
news = {}
page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text, 'html.parser');
all = []
for headline in obj.find_all('div',class_='teaser_conten1'):
    news['Kategori']=json.dumps(headline.find('h1').text) #input kategori berita 
    news['Judul']=json.dumps(headline.find('h2').text) #input judul berita 
    news['WaktuPublish']=json.dumps(headline.find('div', class_='date').text) #input tanggal berita 
    date = datetime.datetime.now()
    today = date.strftime("%A")+", "+date.strftime("%d")+" "+date.strftime("%B")+" "+date.strftime("%Y")
    news['TglPengambilan'] = today #input tanggal pengambilan data 
    #tmp = str(news)
    #tmp = tmp.replace("\"", "")   
    
    all.append (dict(news))
    dzak = all
    print(news)
    with open('headlinedzakira.json', 'w') as file:
        json.dump(all, file, indent=4)


#for headline in obj.find_all('div',class_='teaser_conten1'):

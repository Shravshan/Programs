from bs4 import BeautifulSoup #required to parse html
import requests #required to make request
import re
import datetime
from newspaper import Article
import csv
import time

with open(r'C:\Users\Shravya.Shanmukh\Desktop\Verizon2017_2.csv','r') as f:
    csv_raw_cont=f.read()

split_csv=csv_raw_cont.split('\n')

split_csv.remove('')

separator=","

i=1

for each in split_csv:
    url_row_index=0 #in our csv example file the url is the first row so we set 0
    url = each.split(separator)[url_row_index]
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    article = Article(url)
    try:
        article.download()
        article.parse() 
               
    except:
        myData=[[url,str(i)]]
        out1 = open(r'C:\Users\Shravya.Shanmukh\Desktop\Bad_Links\Bad_Links_2017\Links2017.csv', 'a',encoding='iso-8859-1')
        writer = csv.writer(out1)
        writer.writerows(myData)
        #out1.write(url)
        #out1.write(str(i) + '\n')
        i+=1
        out1.close()
        continue
    
    article.download()
    article.parse() 
    time.sleep(1)
    date=str(article.publish_date)
    regex=r'[^A-Za-z0-9\\ ]'
    out = open(r'C:\Users\Shravya.Shanmukh\Desktop\Output\2017 outputs\Link' + str(i) + '_date_' + date[:10] + '.txt', 'w',encoding='iso-8859-1')
    out.write(re.sub(regex,' ',article.text))
    out.close()
    i+=1
#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup #required to parse html
import requests #required to make request

#read file
with open(r'C:\Users\Shravya.Shanmukh\Desktop\URL.csv','r') as f:
    csv_raw_cont=f.read()

#split by line
split_csv=csv_raw_cont.split('\n')

#remove empty line
split_csv.remove('')

#specify separator
separator=","

#assign a counter
i=0

#iterate over each line
for each in split_csv:
    
    #specify the row index
    url_row_index=0 #in our csv example file the url is the first row so we set 0

    #get the url
    url = each.split(separator)[url_row_index] 

    #fetch content from server
    html=requests.get(url).content

    #soup fetched content
    soup = BeautifulSoup(html,'html.parser')
     
    #creating output files to write the contents to. This will write to 'i' number of files. i=no. of URL's in input CSV    
    out = open(r'C:\Users\Shravya.Shanmukh\Desktop\Output\out' + str(i)+ '.txt', 'w',encoding='utf-8')
    
    #write content from soup
    for link in soup.find_all('p'):
        out.write(link.text)
    out.close()
    #increment counter to read through all URL's
    i+=1

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

#open file to write the contents in
out_single_file=open(r'C:\Users\Shravya.Shanmukh\Desktop\Output\Out.txt', 'a+',newline='',encoding='utf-8')

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

    #show content from soup
    for link in soup.find_all('p'):
        out_single_file.write(link.text)

#close the file        
out_single_file.close()
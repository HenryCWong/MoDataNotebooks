# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:01:47 2019

@author: cywon
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


regex = re.compile(".*?\((.*?)\)")
website_url = requests.get('https://en.wikipedia.org/wiki/List_of_Nobel_laureates_in_Literature').text
soup = BeautifulSoup(website_url,'lxml')
my_table = soup.find('table',{'class':'wikitable sortable'}).tbody
eachRow = my_table.findAll('tr')
allWinners = []

for i in range(len(eachRow)):
    a = eachRow[i].findAll('td')
    if len(a) > 2:
        j = 0
        #print(i)
        #print(len(a))
        if len(a) == 6:
            previousEntry = eachRow[i-1].findAll('td')
            year = previousEntry[j].text.rstrip()
        else:
            year = a[j].text.rstrip()
            j +=1
        picture = a[j]
        j +=1
        name = a[j].text.rstrip()
        j +=1
        country = a[j].text.rstrip()
        country = re.sub("[\(\[].*?[\)\]]", "", country)
        j +=1
        language = a[j].text.rstrip()
        j +=1
        citation = a[j].text.rstrip()
        j +=1
        genres = a[j].text.rstrip()
        #genres = a[j].text.split(',')
        #genres = [x.rstrip() for x in genres]
        allWinners.append([year,name,country,language,citation,genres])
    elif len(a) == 2:
        #print(i)
        year = a[0].text.rstrip()
        laureate = a[1].text.rstrip()
        allWinners.append([year,None,None,None,None,None])
 
#print(allWinners[0])
df = pd.DataFrame(allWinners)
df.to_csv("literature.csv")
#print(my_table.findAll('tr')[1].findAll('td')[4].text)
#my_table = soup.fine('table',{'class':'wikitable sortable'})
#print(my_table.findAll('tr')[1].find_all('td')[5])
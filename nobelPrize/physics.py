# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:01:47 2019

@author: cywon
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
website_url = requests.get('https://en.wikipedia.org/wiki/List_of_Nobel_laureates_in_Physics').text
soup = BeautifulSoup(website_url,'lxml')
my_table = soup.find('table',{'class':'wikitable plainrowheaders sortable'}).tbody
eachRow = my_table.findAll('tr')
allWinners = []

for i in range(len(eachRow)):
    a = eachRow[i].findAll('td')
    #if i == 3:
    #    print(len(a))
    #    print(a)
    if len(a) == 5:
        #print(i)
        #print(len(a))
        year = a[0].text.rstrip()
        #print(year)
        name = eachRow[i].findAll('th')[0].text.rstrip()
        country = a[2].text.rstrip()
        rational = a[3].text.rstrip()
        allWinners.append([year,name,country,rational])
    elif len(a) == 4:
        previousEntry = eachRow[i-1].findAll('td')
        year = previousEntry[0].text.rstrip()
        name = eachRow[i].findAll('th')[0].text.rstrip()
        country = a[1].text.rstrip()
        rational = a[2].text.rstrip()
        allWinners.append([year,name,country,rational])
    elif len(a) == 3:
        previousEntry = eachRow[i-1].findAll('td')
        year = previousEntry[0].text.rstrip()
        name = eachRow[i].findAll('th')[0].text.rstrip()
        country = a[2]
        rational = previousEntry[4].text.rstrip()
        allWinners.append([year,name,country,rational])
    elif len(a) == 2:
        #print(i)
        if "Not awarded" in a[1].text.rstrip():
            year = a[0].text.rstrip()
            rational = a[1].text.rstrip()
            print(rational)
            allWinners.append([year,None,None,rational])
        else:
            previousEntry = eachRow[i-1].findAll('td')
            year = previousEntry[0].text.rstrip()
            name = eachRow[i].findAll('th')[0].text.rstrip()
            country = a[1].text.rstrip()
            #rational= previousEntry[2].text.rstrip()
            #laureate = a[1].text.rstrip()
            allWinners.append([year,name,country,None])
    else:
        print("ERROR!")
        print(a)
        
#print(allWinners[0])
df = pd.DataFrame(allWinners)
df.to_csv("physics.csv")
#print(my_table.findAll('tr')[21].findAll('td')[1].text)
#my_table = soup.fine('table',{'class':'wikitable sortable'})
#print(my_table.findAll('tr')[1].find_all('td')[5])
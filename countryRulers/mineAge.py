# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:11:02 2020

@author: cywon
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
#import wikipediaapi as wp

#wiki_wiki = wp.Wikipedia (language='en',extract_format=wp.ExtractFormat.WIKI)

#p_wiki = wiki_wiki.page("Edi Rama")
#print(p_wiki.text)


#wiki = wp.Wikipedia('en')
#page_py = wiki.page('Edi Rama')
#print("Page - Exists: %s" % page_py.text)

url = "https://en.wikipedia.org/wiki/Edi_Rama"
#url = 'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&titles=Albert_Einstein&format=xml'

fname = "wikipedia.txt"

res = requests.get(url)
soup = BeautifulSoup(res.text, "xml")

birth_re = re.search(r'(detailsBorn.*?\))', soup.getText())
birth_data = re.findall(r'\(([^)]+)', birth_re.group(0))
birth_data = birth_data[0].split("-")
birth_year = birth_data[0]
birth_month = birth_data[1]
birth_day = birth_data[2]
age = 2019 - int(birth_year)
print(age)

#with open(fname,"w",encoding="utf-8") as f:
#    f.write(soup.text)
#birth_data = birth_re.group(0).split('|')
#birth_year = birth_data[2]
#birth_month = birth_data[3]
#birth_day = birth_data[4]

#print(birth_re.group(0).split('|'))

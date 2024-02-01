import bs4 as bs
import urllib
import urllib.request
from pandas import DataFrame
import plotly.graph_objects as go
import numpy as np
import ssl
from IPython.display import display
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context

l=('https://www.screener.in/screen/raw/?query=Market+Capitalization+%3E+1000+AND%0D%0AMarket+Capitalization+%3C+7000')

# check status code for response received 
# success code - 200 
# print(r)
urlpage=urllib.request.urlopen(l)
soup=bs.BeautifulSoup(urlpage,'html.parser')
coulmn=[]
dta=[]
coulmn.append(' ')
soup.find('div',{'class':'responsive-holder fill-card-width'}).findAll('tr')
print("")
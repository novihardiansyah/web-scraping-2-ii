import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json

ctx = ssl.create_default_context() # ssl - Secure Sockets Layer
ctx.check_hostname = False # get hostname to go false
ctx.verify_mode = ssl.CERT_NONE # to pass SSL without certificate

# get the URL to extract HTML so parsing that with BeautifulSoup
url = 'https://www.cia.gov/the-world-factbook/page-data/countries/page-data.json'
print("Opening the file connection...")

uh = urllib.request.urlopen(url, context=ctx) # <http.client.HTTPResponse at 0x2200d6b4888>
print("HTTP status", uh.getcode()) # Get the URL status

html = uh.read().decode() # to read and decode
print(f"Reading done. Total {len(html)} characters read. \n") # Get length of html

getjson = json.loads(html)

smaljson = getjson['result']['data']['countries']['edges']

smaljson2 = len(smaljson)
print(f"{smaljson2} arrays.")

theurl = 'https://www.cia.gov/the-world-factbook/'

country_names=[]
country_url=[]

for idx, val in enumerate(smaljson):
    getjson2 = val['node']['title']
    
    getjson3 = val['node']['uri']
    mixgeturl = theurl + getjson3
    
    country_names.append(getjson2)
    country_url.append(mixgeturl)

demographics1=[]

offset = len('65 years and over:\n')

for idx, val in enumerate(smaljson):
    getjson2 = val['node']['title']
    
    getjson3 = val['node']['uri']
    mixgeturl = theurl + getjson3
    
    
    html = urllib.request.urlopen(mixgeturl, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    txt=soup.get_text()
    pos1=txt.find('0-14 years: ')
    
    if pos1==-1:
        print(f"**0-14 years % data not found for {country_names[idx]}!**")
        demographics1.append(np.nan)
    else:      
        demographics1.append(np.nan)
        text=txt[pos1+12:pos1+18] # number of chars of "0-14 years: "" is 12
        print(text)

''''
Is It Good? -     NDBC NOAA Buoy Output to tell us if it's good out.
Author:  Nick Sepe
License: Git The Unlicense   
Details:  Selecting the NOAA buoy number of your choice, we search for the raw .txt file, clean it up, and spit out the data to a text file.  
+ requests does most of the work 


'''
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt

def now(): # in case we need to compare current time
    print(dt.now())

def file_read(fname):
    content_array = []
    with open(fname) as f:
        for line in f:
            content_array.append(line)
            textArray = open("waveArray.txt","w")
            textArray.write("%s" % content_array)
        print(content_array)

def urlReq(): # no arguments
    buoy = "46224" #change based on your preference
    url = "https://www.ndbc.noaa.gov/data/realtime2/"+buoy+".txt"
    page = requests.get("%s" % url) #request built url
    content = page.content #content is the webpage
    content = content.decode('utf-8') # make nice
    text_file = open("waveFile.txt", "w")
    text_file.write("%s" % content)
    file_read("waveFile.txt")
    
# call function
urlReq()

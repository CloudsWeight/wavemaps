''''
Is It Good? -     NDBC NOAA Buoy Output to tell us if it's good out.
Author:  Nick Sepe
License: Git The Unlicense   
Details:  Selecting the NOAA buoy number of your choice, we search for the raw .txt file, clean it up, and spit out the data to a text file.  
+ requests does most of the work 


'''

import requests
# from bs4 import BeautifulSoup as bs  (only if needed)
from datetime import datetime as dt

def now(): # in case we need to compare current time
    print(dt.now())

def urlReq(): 
    buoy = "46224" #change based on your preference
    url = "https://www.ndbc.noaa.gov/data/realtime2/"+buoy+".txt"
    page = requests.get("%s" % url) #request built url
    content = page.content #content is the webpage
    content = content.decode('utf-8') # make nice
    text_file = open("waveFile.txt", "w") #create waveFile.txt in current directory
    text_file.write("%s" % content) # data is multi-line buoy readings
    print(content)
    
   ## TO DO: create arrays to sort through for each line to compare data
    

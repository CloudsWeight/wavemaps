![image](https://raw.githubusercontent.com/CloudsWeight/wavemaps/main/wavemaps.png)
![image](https://user-images.githubusercontent.com/22231598/144370659-4d961def-1f48-400e-9d4e-16fdec80a194.png)

Example matplotlib graph: https://replit.com/@throwthought/GroupRep#main.py

# ndbcbuoy.py
A python package to scrape NDBC NOAA data, display recent wave heights, or send a text based on user preferences.  ie.) If the waves are over 3 feet you can configure the program to send a text message with the wave height/period.  
* BuoyData() : instantiate a buoy number 
* BuoyData.send_sms(): send a SMS based off user height preference
* BuoyData.set_buoy(buoy#): change the buoy URL
* BuoyData.display_wave_data():  matplotlib chart of recent swell data


# wavemaps.py
Simple prompt to test ndbcbuoy.BuoyData functionality 

# Twilio
* twilio - Requires a twilio.com account for auth_token and account_sid in "send_text.py" ( https://www.twilio.com/try-twilio )


# Usage
* If you have git installed, run [ git clone https://github.com/CloudsWeight/wavemaps ]
* Edit"send_text.py" with your auth_token and account_sid values.
* Then cd into Wave-Maps and run main.py file from the command line [ python3 run.py ]

# Concepts
Using data strcutrued like this: https://www.ndbc.noaa.gov/data/realtime2/46224.txt
* Pull down data from a .txt  
* Clean data using a dictionary and pandas DataFrame 
* Run tests on clean data
* Display clean data
* Send a text message if the data passes our tests.  

# In The Works
Working to display swell height and period inormation in an interactive chart with Django and Highcharts.



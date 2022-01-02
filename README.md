![image](https://user-images.githubusercontent.com/22231598/144370659-4d961def-1f48-400e-9d4e-16fdec80a194.png)

# ndbcbuoy
A python package to scrape NDBC NOAA data, display recent wave heights, or send a text based on pre-defined preferences.  ie.) If the waves are over 3 feet you can configure the program to send a text message with the wave height/period.  

       

# Twilio
* twilio - Requires a twilio.com account for auth_token and account_sid in "send_text.py" ( https://www.twilio.com/try-twilio )


# Usage
    * If you have git installed, run [ git clone https://github.com/CloudsWeight/Wave_Maps ]
    * Edit"send_text.py" with your auth_token and account_sid values.
    * Then cd into Wave_Maps and run main.py file from the command line [ python3 run.py ]

# Concepts
Using data strcutrued like this: https://www.ndbc.noaa.gov/data/realtime2/46224.txt
* Pull down data from a .txt  
* Clean data using a dictionary and pandas DataFrame 
* Run tests on clean data
* Display clean data
* Send a text message if the data passes our tests.  

# In The Works
Working to display swell height and period inormation in an interactive chart with Django and Highcharts.



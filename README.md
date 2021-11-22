# Wave Legend
A python script to scrape NDBC NOAA data for wave heights, wave periods, and more.  If the waves are over 3 feet you can configure the program to send a text message with the wave height/period.  

* Could be convenient to run as a cron job for the lazy surfer.  
* Working to add more functions. 

# imports
* twilio - Requires a twilio.com account for auth_token and account_sid in "send_text.py" ( https://www.twilio.com/try-twilio )
* requests

# Usage
    * If you have git installed, run [ git clone https://github.com/CloudsWeight/Wave_Legend ]
    * Edit"send_text.py" with your auth_token and account_sid values.
    * Then cd into Wave_Legend and run main.py file from the command line [ python3 run.py ]

# Concepts
Using data strcutrued like this: https://www.ndbc.noaa.gov/data/realtime2/46224.txt
* Pull down messy data from a website.  
* Clean up data and organize into relatable items.  
* Store the state of relatable items. 
* Run tests on the state information.
* Send a text message if state passes our tests.  


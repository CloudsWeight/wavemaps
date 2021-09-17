# Wave Legend
A python script to scrape NDBC NOAA data for wave heights, wave periods, and eventually more.  If the waves are over 3 feet you can configure the program to send you a text message with the wave height/period.  

* Could be convenient to run as a cron job for the lazy surfer.  

Plan to develop further.

# imports
twilio, requests

# Requires a twilio account
Just use a free twilio auth and acct id to create a working version for yourself.  

# Concepts
Using information similar to this: https://www.ndbc.noaa.gov/data/realtime2/46224.txt
* Pull down messy data from a website.  
* Clean up data and organize into relatable items.  
* Store the state of relatable items. 
* Run tests on the state information.
* Send a text message if state passes our tests.  


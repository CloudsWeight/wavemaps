''''
Is It Good? -     NDBC NOAA Buoy Output to tell us if it's good out.

Author:  Nick Sepe
License: Git The Unlicense   'git it'

Details:We use urllib to read in the data from a request to our variable [page]
We read page into [servedPage], decode it, then print it to a text file.

'''



import urllib.request
#simple urllib request

# change the http:// to whatever you want to
page = urllib.request.urlopen('https://www.ndbc.noaa.gov/station_page.php?station=46224')
servedPage = page.read()

#make it look better
cleanPage = servedPage.decode("utf-8")

#output the file to the directory we ran the program from
text_file = open("isItGood.txt", "a")
text_file.write("%s" % cleanPage)


# a lot more to do ... 

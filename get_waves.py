'''    get_waves.py - the main 

[Author:  Clouds Weight]
[License: Git The Unlicense]
[Requires:  requests, send_text]
[Creates:
class Buoy [Description: Create Buoy Objects to retrieve buoy data and send a text
    Buoy(number) [number] is the ID of a NDBC buoy
    Methods:
    - urlReq(number) - creates text file of buoy data
    - file_read(file_name) - creates data array from text file
    - clean(data) - returns the last 6 hours of buoy data
    - get_heights(clean_data) - create a zip of ([time],[[height],[period]])
    - decision_to_surf(total) - end decision to send text or not based on data
    - process() - the main() part of the program]
'''
import requests
from send_text import send_text as send

# eventually make the whole thing a class
# to create multiple instances based on buoy number
class Buoy:
    ''' Description: Create Buoy Objects to retrieve buoy data and send a text
    Buoy(number) [number] is the ID of a NDBC buoy
    Methods:
    - urlReq(number) - creates text file of buoy data
    - file_read(file_name) - creates data array from text file
    - clean(data) - returns the last 6 hours of buoy data
    - get_heights(clean_data) - create a zip of ([time],[[height],[period]])
    - decision_to_surf(total) - end decision to send text or not based on data
    - process() - the main() part of the program
    '''
    def __init__(self,buoy_number):
        self.number = buoy_number

    def process(self):
        file = self.urlReq(str(self.number))
        data = self.file_read(file)
        clean_data = self.clean(data)
        total = self.get_heights(clean_data)
        self.decision_to_surf(total)
    # request data file from url, write to waveFile.txt
    def urlReq(self,a_number):
        buoy = a_number
        url = "https://www.ndbc.noaa.gov/data/realtime2/" + buoy + ".txt"
        print(url)
        page = requests.get("%s" % url)  # request built url
        content = page.content  # content is the webpage
        content = content.decode('utf-8')  # make nice
        text_file = open("waveFile.txt", "w")
        text_file.write("%s" % content)
        text_file.close()
        return "waveFile.txt"

    # read the text file and create an array for data manipulation
    def file_read(self,fname):
        content_array = []
        with open(fname) as f:
            for line in f:
                content_array.append(line)
                textArray = open("waveArray.txt", "w")
                textArray.write("%s" % content_array)
        return content_array  # return our new array for data cleaning

    def clean(self,data):
        cleaned = []
        i = 0
        for line in data:
            if i < 12:
                cleaned.append(line)
                i += 1
        return cleaned

    def get_heights(self,clean_data):
        cleaned = clean_data
        time = []
        height = []
        period = []
        for i in cleaned[1:20]:
            time.append(i[10:16])
            height.append(i[33:36])
            period.append(i[39:42])
        waves = zip(height, period)
        total = zip(time, waves)

        return total

    def decision_to_surf(self,total):
    # period = int(period)
        height = list(total)[1]
        period = list(height)[1][1]
        swell = float(list(height)[1][0])
        swell_ft = swell * 3


        if swell > 1.0:
            print(f"The waves look good.  Let's Surf!!")
            send(1, swell_ft, period)
        else:
            print(f"Uhhm.  Maybe don't surf right"
                  f" now.")

def main():
    a = Buoy("46086")
    a.process()



if __name__ == '__main__':
   main()

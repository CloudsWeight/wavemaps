'''
A ndbc buoy data scraping class that:
Creates a dictionary of swell/period for each timestamp.
Charts recent swell and period.
Sends a text message based on user defined paremeters.

'''import requests
import datetime
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class BuoyData:
    ''' Initializes to buoy#46224.  To change #, set_buoy_n(#).  To save the url, set_buoy_url() '''

    def __init__(self):
        self.N = 33
        self.set_buoy_n()
        self.set_buoy_url()
        self.save_content_to_file()

    def __repr__(self):
        return {self.buoy:self.url}

    def __str__(self):
        return self.url

    def set_buoy_n(self, n = '46268'):
        self.buoy = n
        self.set_buoy_url()
        return n

    def set_buoy_url(self):
        # allow user to change buoy number
        buoy = str(self.buoy)
        url = "https://www.ndbc.noaa.gov/data/realtime2/" + buoy + ".txt"
        self.url = url
        return self.url

    def get_time_str(self):
        #set timestamp to string to add to text files
        now = datetime.datetime.now()
        now_str = now.strftime("%d_%m_%Y_%H_%M")
        return now_str

    def get_url_content(self):
        page = requests.get(self.url)
        content = page.content
        # format and decode page response
        content = content.decode('utf-8')
        return content

    def save_content_to_file(self):
        content = self.get_url_content()
        # create a time stamp for files if necessary, un-comment both below
        #now_str = self.get_time_str()
        #self.file_name = f'{now_str}waves.txt'
        self.file_name ="waves.txt"
        text_file = open(self.file_name, "w")
        text_file.write(content)
        text_file.close()
        return self.file_name

    def create_list_from_content(self):
        # read each line and store in a list
        details_list = []
        with open(self.file_name) as f:
            for line in f:
                details_list.append(line)
        return details_list  # return data cleaning list

    def set_sample_size(self, N=33):
        self.N = N
        return self.N

    def clean_list_data(self):
        details_list = self.create_list_from_content()
        # select only last N  list items for calculations
        cleaned_data = []
        i = 0
        for line in details_list:
            if i < self.N:
                cleaned_data.append(line)
                i += 1
        return cleaned_data

    def create_wave_dict(self):
        cleaned_data = self.clean_list_data()
        wave_data = {}
        n = 0
        for i in cleaned_data[2::2]:
            wave_data[n] = [i[4:16], float("{:.2f}".format(float(i[33:36])*3.281)),float("{:.2f}".format(float(i[39:42])))]
            n +=1
        return wave_data

    def get_dataframe(self):
        df = pd.DataFrame(self.create_wave_dict())
        return df

    def display_wave_data(self):
        x , y1, y2 = [], [], []
        wave_data = self.buoy_request()
        print(wave_data.items())
        for i in wave_data.items():
            x.append(i[1][0])
            y1.append(i[1][1])
            y2.append(i[1][2])
        x.reverse()
        y1.reverse()
        y2.reverse()
        plt.plot(x, y1, label ='ft')
        plt.plot(x,y2, label='sec')
        plt.show()


    def save_buoy_details(self):
            deets = self.create_list_from_content()
            return deets

    def buoy_request(self):
        deets = self.save_buoy_details()
        cleaned_data = self.clean_list_data()
        waves = self.create_wave_dict()
        #self.display_wave_data(waves)
        return waves

    def show_graph(self):
        self.display_wave_data(self.process_buoy_request())

def main():
    a = BuoyData()
    print(a.display_wave_data())

if __name__ =="__main__":
    main()

'''
Some other working buoy numbers, becaus  not all buoy numbers work:
    -  46268 ; Topanga Nearshore, CA
    -  44097; Block Island, RI
    -

List of ndbc stations: https://www.ndbc.noaa.gov/to_station.shtml

'''

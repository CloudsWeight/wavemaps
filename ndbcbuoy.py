'''
A ndbc buoy data scraping class that:
Creates a dictionary of swell/period for each timestamp.
Charts recent swell and period.
Sends a text message based on user defined paremeters.

'''
import requests
import datetime
import time
import matplotlib.pyplot as plt
import numpy as np

class BuoyData:
    ''' Initializes to 46224, change BuoyData.buoy to another number, and save the url, BuoyData.set_buoy_url() '''
    def __init__(self):
        self.set_buoy_n()
        self.set_buoy_url()
        self.save_content_to_file()

    def __repr__(self):
        return {self.buoy:self.url}

    def __str__(self):
        return self.url

    def set_buoy_n(self, n = 46224):
        self.buoy = n
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
        #built_ts = f'{now_str}waves.txt'
        self.file_name ="waves.txt"
        text_file = open(self.file_name, "a")
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

    def clean_list_data(self):
        details_list = self.create_list_from_content()
        # select only last N  list items for calculations
        cleaned_data = []
        N = 33
        i = 0
        for line in details_list:
            if i < N:
                cleaned_data.append(line)
                i += 1
        return cleaned_data

    def create_wave_dict(self):
        cleaned_data = self.clean_list_data()
        wave_data = {}
        for i in cleaned_data[2::3]:
            wave_data[i[4:16]] = (float("{:.2f}".format(float(i[33:36])*3.281)),float("{:.2f}".format(float(i[39:42]))))
            #height.append(float("{:.2f}".format(float(i[33:36]))*3.281))
        return wave_data

    def display_wave_data(self):
        x = []
        y = []
        wave_data = self.buoy_request()
        for i in wave_data.items():
            x.append(i[0])
            y.append(i[1])
        x.reverse()
        y.reverse()
        plt.plot(x,y)
        plt.show()
        return wave_data

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
    a.display_wave_data()


if __name__ =="__main__":
    main()


'''
https://www.ndbc.noaa.gov/to_station.shtml

list of ndbc stations

'''

import requests
import datetime
import time
import matplotlib.pyplot as plt

class BuoyData:
    def __init__(self):
        self.buoy = 46224
    def get_time_str(self):
        #set timestamp to string to add to text files
        now = datetime.datetime.now()
        now_str = now.strftime("%d_%m_%Y_%H_%M")
        return now_str


    def request_buoy_url(self):
        # allow user to change buoy number
        buoy = str(self.buoy)
        url = "https://www.ndbc.noaa.gov/data/realtime2/" + buoy + ".txt"
        self.url = url
        return self.url

    def get_url_content(self, url):
        page = requests.get(url)
        content = page.content
        # format and decode page response
        content = content.decode('utf-8')
        return content

    def save_content_to_file(self, content):
        # save a timestamped text file named waves_[t/s]
        now_str = self.get_time_str()
        file_name = f"waves_{now_str}.txt"
        text_file = open(file_name, "w")
        text_file.write(content)
        text_file.close()
        return file_name

    def save_file_content_to_list(self, file):
        # read each line and store in a list
        details_list = []
        with open(file) as f:
            for line in f:
                details_list.append(line)
        return details_list  # return data cleaning list

    def clean_list_data(self, details_list):
        # select only last N  list items for calculations
        cleaned_data = []
        N = 33
        i = 0
        for line in details_list:
            if i < N:
                cleaned_data.append(line)
                i += 1
        return cleaned_data

    def get_wave_data(self, cleaned_data):
        time = []
        height = []
        period = []
        for i in cleaned_data[2::3]:
            time.append(i[4:16])
            height.append(float("{:.2f}".format(float(i[33:36])*3.281)))
            period.append(float(i[39:42]))
            wave_data = [time, height, period]
        return wave_data

    def display_wave_data(self, wave_data):
        length = len(wave_data[0])
        x = wave_data[0]
        x = x[::-1]
        y = wave_data[1]
        y = y[::-1]
        plt.plot(x,y)
        #plt.subplots(constrained_layout=True)
        plt.ylabel('Wave Height- ft')
        plt.show()

    def process_buoy_request(self):

        url = self.request_buoy_url()
        content = self.get_url_content(url)
        file_name = self.save_content_to_file(content)
        deets = self.save_file_content_to_list(file_name)
        cleaned_data = self.clean_list_data(deets)
        waves = self.get_wave_data(cleaned_data)
        self.display_wave_data(waves)

    def show_graph(self):
        self.process_buoy_request()

def main():
    a = BuoyData()
    a.process_buoy_request()

if __name__ =="__main__":
    a = BuoyData()
    a.show_graph()


'''
https://www.ndbc.noaa.gov/to_station.shtml

list of ndbc stations

'''

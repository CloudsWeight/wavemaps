'''

 Wave Legend - Map and Alert of Local Ocean Swells Using Latest NDBC NOAA Buoy Buoy Data
Details:  Selecting the NOAA buoy number of your choice, we search for the raw .txt file, clean up the data,
make decisions on the data, and if we like the wave data we send text message with the happy data.


Author:  Clouds Weight
License: Git The Unlicense

   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(      
`-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `

       ,(   ,(   ,(   ,(   ,  W A V E                   ,(  ,(   ,(   ,(   ,(   ,(   ,(      
    `-'  `-'  `-'  `-'  `-'            L E G E N D   `-' `-'  `-'  `-'  `-'  `-'  `-'  `

           ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(      
        `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `
'''

from get_waves import Buoy

def main():
    a = Buoy("46224")
    a.process()

if __name__ == "__main__":
    main()

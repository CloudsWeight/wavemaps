'''

 Wave Maps - Map and SMS package for NDBC NOAA Buoy Buoy Data

Author:  Clouds Weight
License: Git The Unlicense

   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(
`-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `

       ,(   ,(   ,(   ,(   ,  W A V E                   ,(  ,(   ,(   ,(   ,(   ,(   ,(
    `-'  `-'  `-'  `-'  `-'               M A P S    `-' `-'  `-'  `-'  `-'  `-'  `-'  `

           ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(
        `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `
'''
from ndbcbuoy import BuoyData

def prompt():
    ans = int(input("\n | Options are displayed below. |" \
        "\n #######################" \
        "\n1.)Display the recent swell" \
        "\n2.) Send a text if it's good" \
        "\n3.) Exit" \
        "\n Enter a number: "))
    return ans

def main():
    a = BuoyData()
    print("\n        WELCOME TO WAVE MAPS!" \
    "\n        ,(   ,(   ,(   ,(   ,    W A V E              ,(   ,(   ,(   ,(   ,(   ,(" \
    "\n         `-'  `-'  `-'  `-'  `-'             M A P S    `-' `-'  `-'  `-'  `-'  `-'  `-'  `  `"  "\n     ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,(   ,( " \
    "\n    `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-'  `-' " )
    while True:
        ans = prompt()
        if ans == 1:
            a.display_wave_data()

        elif ans == 2:
            a.send_sms()

        elif ans == 3:
            print('Bye bye.')
            break
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Looks like you tried a different option.")
            print("Try another option.  1... 2... 3...")



if __name__ == "__main__":
    main()

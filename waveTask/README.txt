Configuration instructions to create a .exe scheduled task for Wave Maps text functionality.
#################################################################################################################
The tasker.py file requires a twilio sid_key and auth_token which can be downloaded from TWILIO.COM.            

Replace the necessary values in the tasker.py source code, it should be obvious once you read it.              
HINT: self.account_sid_key and self.auth_token_key need your twilio info

Replace the to and from phone numbers with your own info.

To create the .exe for the file you will need to pip install "pyinstaller" ( pip3 install pyinstaller )

After editing the tasker.py file with your TWILIO information, navigate to the folder with the tasker.py file from command line, then Run [ pyinstaller -onefile tasker.py ] 

This will create a dist folder with the tasker.exe file in it, this is your .exe file for the python script.

Now just create  scheduled task in windows with Task Scheduler :)

TO DO:  Create bat files for pip installing pyinstaller and creating a task 

##################################################################################################################

'''  SAMPLE TO SEND TeXT MESSAGE
USE FOR TESTING THIS SHOULD NOT BE INCLUDED IN ANY PROGRAM YET

Try and make it OOP
'''

#!/bin/python

from twilio.rest import Client
'''
account_sid = ""# you know what it is
auth_token = ""
client = Client(account_sid, auth_token)
client.messages.create(
    to="+",#verified phone to send to most likely your own phone number
    from_="+",#twilion phone number
    body="Taco Fiesta A La Playa!  "
)
'''
def send_text(true, height, period):
    if true >= 1:
        height = height
        period = period
        account_sid = ""
        auth_token = ""
        client = Client(account_sid, auth_token)
        client.messages.create(
            to="+",#verified phone to send to most likely your own phone number
            from_="+",#twilion phone number
            body=f"Go surf the waves are {height}ft @{period}sec !! \
            Check out the latest details at http://phaseassay.com"
        )

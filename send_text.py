'''  SAMPLE TO SEND TeXT MESSAGE
USE FOR TESTING THIS SHOULD NOT BE INCLUDED IN ANY PROGRAM YET

Try and make it OOP
'''

#!/bin/python

from twilio.rest import Client
'''
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)
client.messages.create(
    to="+19495219358",
    from_="+15103067958",
    body="Taco Fiesta A La Playa!  "
)
'''
def send_text(true, height, period):
    if true >= 1:
        height = height
        period = period
        account_sid = "AC6b88e76ab99311def0fb9a76bc14af51"
        auth_token = "d5b6f2f9fb64da3b0a67278a7d1a3ad0"
        client = Client(account_sid, auth_token)
        client.messages.create(
            to="+19495219358",
            from_="+15103067958",
            body=f"Go surf the waves are {height}ft @{period}sec !! \
            Check out the latest details at http://phaseassay.com"
        )

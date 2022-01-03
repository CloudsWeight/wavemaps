'''  Function to send text using auth and acct id fromt twilio'''
from twilio.rest import Client
from twiliokey import TwilioKey

def send_text(height, period):
    ''' Requires a height and period variable, 
    SMS decision is based on height.  '''
    key = TwilioKey()
    height = float("{:.2f}".format(height))
    period = period
    account_sid = key.get_sid()
    auth_token = key.get_auth()
    client = Client(account_sid, auth_token)
    sms_body = f"Wave Maps - Go surf! Waves are {height}ft @{period}sec \n" \
    "- <3 your friends from http://phaseassay.com"
    client.messages.create(
        to="+", # this is the phone to receive the text
        from_="+", # this is the twilio assigned SMS #
        body= sms_body)
    return sms_body

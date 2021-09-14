'''  Function to send text using auth and acct id fromt twilio 
'''

from twilio.rest import Client

def send_text(true, height, period):
    if true >= 1:
        height = height
        period = period
        account_sid = ""# you know what it is
        auth_token = ""
        client = Client(account_sid, auth_token)
        client.messages.create(
            to="+",#verified phone to send to most likely your own phone number
            from_="+",# twilio phone number to send texts
            body=f"Go surf the waves are {height}ft @{period}sec !! \
            Check out the latest details at http://phaseassay.com"
        )

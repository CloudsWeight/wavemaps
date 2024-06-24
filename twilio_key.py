''' Twilio keys for send_text.py:
account_sid_key
auth_token
'''
class TwilioKey:
    def __init__(self): # https://www.twilio.com/try-twilio
        self.account_sid_key = "your_sid"
        self.auth_token_key = "your_auth"

    def get_sid(self):
        return self.account_sid_key

    def get_auth(self):
        return self.auth_token_key

from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC3f1c1c79a2800ba14607904adff70456"
auth_token  = "9d36187f4d0f53824544096b5cda667d"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="This is a twilio test. It Works!",
    to="+18586102390",    # Replace with your phone number
    from_="+18583465509") # Replace with your Twilio number
print message.sid

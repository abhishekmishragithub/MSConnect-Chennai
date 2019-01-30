# Download the library from https://www.twilio.com/docs/python/install OR
# pip install twilio
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'Axx8'
auth_token = '3xxe'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Welcome to MS Connect(); Chennai,\
                     Empowering every developer to achieve more !! ",
                     from_='+17xx8',
                     to='+91xx4'
                 )

print(message.sid)
print("Message Sent Successfully !")

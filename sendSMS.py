# from twilio.rest import Client
# account_sid='ACed38494fdb2dd50505a2df20f8b00c20'
# auth_token='acf7b4af2a59e57151a061da9c5044e1'
# client=Client(account_sid,auth_token)
# client.messages.create(
#     to='+91 9870216540',
#     from_='17015436151',
#     body='Hi this is kumar mayank'
#     )

from twilio.rest import Client

def send(msg):
    account_sid="ACed38494fdb2dd50505a2df20f8b00c20"
    auth_token="acf7b4af2a59e57151a061da9c5044e1"
    client=Client(account_sid, auth_token)
    if msg:
        client.messages.create(
        to="+917291872075",
        from_="+17015436151",
        body=msg)
    else:
        client.messages.create(
        to="+917291872075",
        from_="+17015436151",
        body="I am at MSHacks 2.0")

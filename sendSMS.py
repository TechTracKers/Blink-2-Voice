from twilio.rest import Client

def send(msg):
    account_sid="your auth_id"
    auth_token="your auth_token"
    client=Client(account_sid, auth_token)
    if msg:
        client.messages.create(
        to="123456789",
        from_="123456789",
        body=msg)
    else:
        client.messages.create(
        to="123456789",
        from_="123456789",
        body="Hello")

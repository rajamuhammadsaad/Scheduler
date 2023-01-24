from twilio.rest import Client
account_sid = 'XXXX' # Add your Twilio Account's SID
auth_token = 'XXX' # Add your Twilio Account's Auth Token
client = Client(account_sid, auth_token)
def send_rem(date,rem):
  message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='*REMINDER* '+date+'\n'+rem,
  to='whatsapp:XXX' # Add your WhatsApp No. here
)
print(message.sid)
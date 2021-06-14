
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account_sid = os.environ['ASJ34638HSJFSDJF3489']
#auth_token = os.environ['SHDFKSFJKSFJUW65247H']
def sleepy():
    client = Client("ASJ34638HSJFSDJF3489", "SHDFKSFJKSFJUW65247H")  # put account id and token from your twilio.

    message = client.messages \
        .create(
        body='Alert!..Alert!!..Alert!!! Drowsiness detection....xyz feeling drowsy',
        from='+1234456',    # this is sample number instead of that put that number which gives twilio.
        to='+919876543210'   # exist mobile number but that number is registered on twilio.
    )

    print(message.sid)

def yawn():
    client = Client("ASJ34638HSJFSDJF3489", "SHDFKSFJKSFJUW65247H")

    message = client.messages \
        .create(
        body='Alert!..Alert!!..Alert!!!yawning dectect....xyz Needs refreshment',
        from_='+123456',                         # this is sample number instead of that put that number which gives twilio
        to='+919876543210'   # exist mobile number but that number is registered on twilio
    )

    print(message.sid)



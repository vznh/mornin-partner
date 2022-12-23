from twilio.rest import Client
from encryption import account_sid, auth, pn
from message import compose
from database import db

def sendInit():
    # First, let's set up the Twilio client
    client = Client(account_sid, auth)
    for person in range(len(db)):
        message = client.messages.create(
            to=db[person].returnPhoneNumber(),
            from_=pn,
            body=compose(db[person])
    )
    print(f"Sent {len(db)} message(s) with SID: {message.sid}")

from flask import Flask, request, Response

app = Flask(__name__)
client = Client(account_sid, auth)

@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    # Get the incoming message details
    message_sid = request.form["MessageSid"]
    message_body = request.form["Body"]
    from_number = request.form["From"]

    # Do something with the message
    if "hello" in message_body.lower():
        response_message = "Hello there! How can I help you?"
    elif "goodbye" in message_body.lower():
        response_message = "Goodbye! Have a great day."
    else:
        response_message = "I'm sorry, I didn't understand your message. Could you please rephrase it?"

    # Send a reply
    message = client.messages.create(
        to="+14085181282",
        from_=pn,
        body=response_message
    )

    # Return a empty response
    return Response(), 200

if __name__ == "__main__":
    sendInit()
    app.run(debug=True)
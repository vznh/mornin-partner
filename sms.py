from twilio.rest import Client
from encryption import account_sid, auth, pn
from message import compose
from database import db
from person import Person
from fc import *

def sendInit():
    client = Client(account_sid, auth)
    for person in range(len(db)):
        db[person].loadReminders()
        message = client.messages.create(
            to=db[person].returnPhoneNumber(),
            from_=pn,
            body=compose(db[person])
    )
    print(f"Sent {len(db)} message(s) with SID: {message.sid}")

from flask import Flask, request, Response

app = Flask(__name__)
client = Client(account_sid, auth)

@app.route("/sms", methods=["POST"])
def smsReply():
    # Get the incoming message details
    message_sid = request.form["MessageSid"]
    message_body = request.form["Body"]
    from_number = request.form["From"]
    for person in db:
        if person.pn == from_number:
            user = person

    # Do something with the message
    if "cmd" in message_body.lower():
        response_message = f'''commands available:
"remind me: [reminder] - Use the keyword "remind me:" to start a reminder. 
You'll be reminded about it the next morning.
"clear rm" - clears all reminders
"STOP" - ceases text contact
"sports [sports name]" // not implemented - Presents live sports games available. When prompted, returns score and status of live game.
"traffic [highway] // not implemented - Returns congestion status of highway'''


    elif "remind" in message_body.lower():
        rm = message_body.lower().split(" ")
        for i, word in enumerate(rm):
            if ":" in word:
                del rm[:i+1]
                break

        rm = " ".join(rm)
        user.addReminder(rm)
        print(from_number)
            
        response_message = f"added '{rm}' to your reminders!\nʚ♡⃛ɞ(ू•ᴗ•ू❁)\n\nhere's what you need to know:\n{user.msg()}"
    elif "clear rm" in message_body.lower():
        user.clearReminder()
        response_message = "reminders cleared!"
    elif "sports" in message_body.lower():
        for i, word in enumerate(rm):
            if "sports" in word:
                del rm[:i+1]
                break
    else:
        response_message = "i dont know what the fuck u sayin dawg try using 'help' for more commands"

    # Send a reply
    message = client.messages.create(
        to=from_number,
        from_=pn,
        body=response_message
    )

    # Return a empty response
    return Response(), 200

if __name__ == "__main__":
    sendInit()
    app.run(debug=True    )
from person import Person
from database import db
from fc import requestNews, requestWeather
from twilio.rest import Client
from encryption import account_sid, pn, auth
from st import st
from random import randint

def compose(user):
    message = ""
    
    userdata = Person.getUserData(user)
    # Creating the good morning part
    message += f"Hello {user.name}! {st[randint(0,len(st)-1)]}\n"
    
    # Weather api
    weatherData = requestWeather(user.city)
    message += f"\nWeather is looking like {weatherData[4]}.\n"
    message += f"Today, it feels like {weatherData[1]:.0f}° degree fahrenheit.\n"
    message += f"Looks like low of {weatherData[2]:.0f}°, and high of {weatherData[3]:.0f}° degrees.\n"

    message += "\n"
    # Reminder api
    if user.checkReminders() == True:
        message += f"You have {len(user.reminders)} reminder(s) :)\n"
        
        for _ in range(len(user.reminders)):
            message += f"{_+1}. {user.reminders[_]}\n"
    
    else:
        message += f"You have no reminders at this time.\n"

    # News api
    articles = requestNews()
    message += "\nNews for today:\n"
    for ar in range(len(articles)):
        message += f"{ar+1}. {articles[ar]}\n"

    # Traffic conditions api
    pass
    return message
    
if __name__ == '__main__':

    client = Client(account_sid, auth)
    for person in range(len(db)):
        msg = client.messages \
        .create(
            body=compose(db[person]),
            from_=pn,
            to=db[person].returnPhoneNumber()
    )
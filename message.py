from person import Person
from database import db
from fc import requestNews, requestWeather
from st import st, gm
from random import randint

def compose(user):
    message = ""

    # Creating the good morning part
    message += f"{gm[randint(0,len(gm)-1)]} {user.name}!\n{st[randint(0,len(st)-1)]}\n"
    
    # Weather api
    weatherData = requestWeather(user.city)
    message += f"\nWeather is looking like {weatherData[4]} for {user.city}.\n"
    message += f"Today, it feels like {weatherData[1]:.0f}° degree fahrenheit.\n"
    message += f"Looks like low of {weatherData[2]:.0f}°, and high of {weatherData[3]:.0f}° degrees.\n"
    message += "\n"

    # Reminder 
    if user.checkReminders() == True:
        message += f"Here are your reminder(s) :)\n"
        message += user.msg()
    else:
        message += f"You have no reminders at this time.\n"

    # News api
    #articles = requestNews()
    #message += "\nNews for today:\n"
    #for ar in range(len(articles)):
    #    message += f"{ar+1}. {articles[ar]}\n"

    # Traffic conditions api
    pass
    message += "\n\nrun 'cmd' for more help" 
    return message

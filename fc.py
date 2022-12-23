# Let's start with APIs.
# We will pull weather data.
import requests
from encryption import wapi, napi, tapi # Importing api keys

def requestWeather(city):
    report = []
    api = wapi
    base = "https://api.openweathermap.org/data/2.5/weather?"
    final = base + "q=" + city + "&appid=" + api
    response = requests.get(final)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather']

        report.append(main['temp']) # [0]
        report.append(main['feels_like']) # [1]
        report.append(main['temp_min']) # [2]
        report.append(main['temp_max']) # [3]
        report.append(weather[0]['description']) # [4]

    else:
        print(f"{response.status_code}: Not working.")

    report = [ (x-273.15)*1.8+32 if type(x) == float else x for x in report ]
    return report

# We will now pull global news data.
def requestNews():
    articles = []
    queryparams = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": napi
    }
    main_url = "https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=queryparams)
    open_bbc_page = res.json()

    article = open_bbc_page["articles"] # sorts
    results = []

    for ar in article: # sorts again
        results.append(ar["title"])

    for i in range(3):
        articles.append(results[i])

    return articles

def requestTraffic(city):
    queryparams = {

    }
    base = "api.tomtom.com"
    main = "https://" + base + "/traffic/trafficstats/status/1/{job_id}?key={Your_API_Key}"
    res = requests.get(main)
    print(res)

# Reminder section 
from person import Person
def addReminder(person: Person, reminder):
    person.addReminder(reminder)
    with open(f"{person.name}rm.txt", "a+") as f:
        f.write(f"{reminder}\n")
    
def removeReminder(person: Person, reminder):
    person.removeReminder(reminder)
    with open(f"{person.name}rm.txt", "w+") as f:
        for _ in range(len(person.reminders)):
            f.write(f"{person.reminders[_]}\n")


# Sports API pulling for live matches
# We'll be using Python Requests in order to obtain results
import requests
from encryption import sapi

# We'll start with football.
def footballLive():
    url = "https://sports-live-scores.p.rapidapi.com/football/live"

    headers = {
        "X-RapidAPI-Key": sapi,
        "X-RapidAPI-Host": "sports-live-scores.p.rapidapi.com"
    }

    currentGames = {}
    currentScores = {}
    response = requests.request("GET", url, headers=headers)
    response = response.json()
    games = response["matches"]
    c = 0
    for game in games:
        currentGames[f"Result {c+1}"] = f"{game['Home Team']} vs. {game['Away Team']}\n{game['League']}, currently in {game['Status']}"
        currentScores[f"Result {c+1}"] = f"{game['Home Score']} to {game['Away Score']}"
        c += 1
    
    x = input("Which game would you like to pick?\n").lower()
    x = x.strip("game")
    x = int(x)
    message += currentGames[f"Result {x}"]
    message += "\n"
    message += currentScores[f"Result {x}"]
    return message

# Then tennis.
def tennisLive():
    url = "https://sports-live-scores.p.rapidapi.com/tennis/live"

    headers = {
        "X-RapidAPI-Key": sapi,
        "X-RapidAPI-Host": "sports-live-scores.p.rapidapi.com"
    }

    currentGames = {}
    currentScores = {}
    response = requests.request("GET", url, headers=headers)
    response = response.json()
    games = response["matches"]
    c = 0
    for game in games:
        currentGames[f"Result {c+1}"] = f"{game['Home Team']} vs. {game['Away Team']}\n{game['League']}, currently in {game['Status']}"
        currentScores[f"Result {c+1}"] = f"{game['Home Score']} to {game['Away Score']}"
        c += 1
    
    x = input("Which game would you like to pick?\n").lower()
    x = x.strip("game")
    x = int(x)
    message += currentGames[f"Result {x}"]
    message += "\n"
    message += currentScores[f"Result {x}"]
    return message

# Then basketball.
def basketballLive():
    message = ""
    url = "https://sports-live-scores.p.rapidapi.com/basketball/live"

    headers = {
        "X-RapidAPI-Key": sapi,
        "X-RapidAPI-Host": "sports-live-scores.p.rapidapi.com"
    }
    
    currentGames = {}
    currentScores = {}
    response = requests.request("GET", url, headers=headers)
    response = response.json()
    games = response["matches"]
    c = 0
    for game in games:
        currentGames[f"Result {c+1}"] = f"{game['Home Team']} vs. {game['Away Team']}\n{game['League']}, currently in {game['Status']}"
        currentScores[f"Result {c+1}"] = f"{game['Home Score']} to {game['Away Score']}"
        c += 1
    
    x = input("Which game would you like to pick?\n").lower()
    x = x.strip("game")
    x = int(x)
    message += currentGames[f"Result {x}"]
    message += "\n"
    message += currentScores[f"Result {x}"]
    return message

# Then baseball.
def baseballLive():
    url = "https://sports-live-scores.p.rapidapi.com/baseball/live"

    headers = {
        "X-RapidAPI-Key": sapi,
        "X-RapidAPI-Host": "sports-live-scores.p.rapidapi.com"
    }

    currentGames = {}
    currentScores = {}
    response = requests.request("GET", url, headers=headers)
    response = response.json()
    games = response["matches"]
    c = 0
    for game in games:
        currentGames[f"Result {c+1}"] = f"{game['Home Team']} vs. {game['Away Team']}\n{game['League']}, currently in {game['Status']}"
        currentScores[f"Result {c+1}"] = f"{game['Home Score']} to {game['Away Score']}"
        c += 1
    
    x = input("Which game would you like to pick?\n").lower()
    x = x.strip("game")
    x = int(x)
    message += currentGames[f"Result {x}"]
    message += "\n"
    message += currentScores[f"Result {x}"]
    return message

class Sport:
    def footballLive():
        url = "https://sports-live-scores.p.rapidapi.com/football/live"

        headers = {
            "X-RapidAPI-Key": sapi,
            "X-RapidAPI-Host": "sports-live-scores.p.rapidapi.com"
        }

        currentGames = {}
        currentScores = {}
        response = requests.request("GET", url, headers=headers)
        response = response.json()
        games = response["matches"]
        c = 0
        for game in games:
            currentGames[f"Result {c+1}"] = f"{game['Home Team']} vs. {game['Away Team']}\n{game['League']}, currently in {game['Status']}"
            currentScores[f"Result {c+1}"] = f"{game['Home Score']} to {game['Away Score']}"
            c += 1
        
        x = input("Which game would you like to pick?\n").lower()
        x = x.strip("game")
        x = int(x)
        message += currentGames[f"Result {x}"]
        message += "\n"
        message += currentScores[f"Result {x}"]
        return message

    # Then tennis.
    def tennisLive():
        url = "https://sports-live-scores.p.rapidapi.com/tennis/live"

        headers = {
            "X-RapidAPI-Key": sapi,
            "X-RapidAPI-Host": "sports-live-scores.p.rapidapi.com"
        }

        currentGames = {}
        currentScores = {}
        response = requests.request("GET", url, headers=headers)
        response = response.json()
        games = response["matches"]
        c = 0
        for game in games:
            currentGames[f"Result {c+1}"] = f"{game['Home Team']} vs. {game['Away Team']}\n{game['League']}, currently in {game['Status']}"
            currentScores[f"Result {c+1}"] = f"{game['Home Score']} to {game['Away Score']}"
            c += 1
        
        x = input("Which game would you like to pick?\n").lower()
        x = x.strip("game")
        x = int(x)
        message += currentGames[f"Result {x}"]
        message += "\n"
        message += currentScores[f"Result {x}"]
        return message

    # Then basketball.
    def basketballLive():
        message = ""
        url = "https://sports-live-scores.p.rapidapi.com/basketball/live"

        headers = {
            "X-RapidAPI-Key": sapi,
            "X-RapidAPI-Host": "sports-live-scores.p.rapidapi.com"
        }
        
        currentGames = {}
        currentScores = {}
        response = requests.request("GET", url, headers=headers)
        response = response.json()
        games = response["matches"]
        c = 0
        for game in games:
            currentGames[f"Result {c+1}"] = f"{game['Home Team']} vs. {game['Away Team']}\n{game['League']}, currently in {game['Status']}"
            currentScores[f"Result {c+1}"] = f"{game['Home Score']} to {game['Away Score']}"
            c += 1
        
        x = input("Which game would you like to pick?\n").lower()
        x = x.strip("game")
        x = int(x)
        message += currentGames[f"Result {x}"]
        message += "\n"
        message += currentScores[f"Result {x}"]
        return message

    # Then baseball.
    def baseballLive():
        url = "https://sports-live-scores.p.rapidapi.com/baseball/live"

        headers = {
            "X-RapidAPI-Key": sapi,
            "X-RapidAPI-Host": "sports-live-scores.p.rapidapi.com"
        }

        currentGames = {}
        currentScores = {}
        response = requests.request("GET", url, headers=headers)
        response = response.json()
        games = response["matches"]
        c = 0
        for game in games:
            currentGames[f"Result {c+1}"] = f"{game['Home Team']} vs. {game['Away Team']}\n{game['League']}, currently in {game['Status']}"
            currentScores[f"Result {c+1}"] = f"{game['Home Score']} to {game['Away Score']}"
            c += 1
        
        x = input("Which game would you like to pick?\n").lower()
        x = x.strip("game")
        x = int(x)
        message += currentGames[f"Result {x}"]
        message += "\n"
        message += currentScores[f"Result {x}"]
        return message





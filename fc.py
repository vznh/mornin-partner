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


if __name__ == "__main__":
    requestTraffic("Milpitas")



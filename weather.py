import requests as req
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

url = "https://api.weatherapi.com/v1/forecast.json"

def get_weather(city, days):
    params = {
        "key": api_key,
        "q": city,
        "days": int(days),  # Number of days to forecast
        "alerts": "yes"  # Include weather alerts in the response
    }
    try:
        response = req.get(url, params=params)
    except req.exceptions.RequestException:
        print(f"Error: Unable to connect to the weather service." +
              f" Please check your internet connection and try again.")
        return None

    if response.status_code == 200:
        data = response.json()
        condition = data['current']['condition']['text']
        emoji = get_weather_emoji(condition)
        forecast_days = data['forecast']['forecastday']
        alerts = data['alerts']['alert']

        weather = {
            "city_name": data['location']['name'],
            "country": data['location']['country'],
            "temperature_c": data['current']['temp_c'],
            "temperature_f": data['current']['temp_f'],
            "condition": condition,
            "emoji": emoji,
            "humidity": data['current']['humidity'],
            "wind_speed": data['current']['wind_mph'],
            "forecast": forecast_days,
            "alerts": alerts
        }
        return weather
    else:
        data = response.json()

        print("HTTP Status Code:", response.status_code)
        print("API Error Code:", data["error"]["code"])
        print("Error Message:", data["error"]["message"])

        return None

#emoji
weather_emojis = {
    "Sunny": "☀️ ",
    "Partly cloudy": "⛅ ",
    "Cloudy": "☁️ ",
    "Overcast": "🌥️ ",
    "Mist": "🌫️ ",
    "Light rain": "🌧️ ",
    "Moderate rain": "🌧️ ",
    "Heavy rain": "🌧️ ",
    "Light snow": "🌨️ ",
    "Moderate snow": "🌨️ ",
    "Heavy snow": "🌨️ "
}
def get_weather_emoji(condition):
    return weather_emojis.get(condition, "🌤️ ")


def plot_temperature(forecast_days):
    plt.title("Weather Graph")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    dates = []
    max_temps = []
    min_temps = []

    for day in forecast_days:
        dates.append(day["date"])
        max_temps.append(day["day"]["maxtemp_c"])
        min_temps.append(day["day"]["mintemp_c"])
    plt.plot(dates, max_temps, marker = "o", label = "Max temp")
    plt.plot(dates, min_temps, marker = "o", label = "Min temp")
    plt.legend()
    plt.grid(True)

    plt.show()


def print_weather_report(weather):
        print("|----------------------------|")
        print("|       Weather Report       |")
        print("|----------------------------|")

        print("City:", weather["city_name"])
        print("Country:", weather["country"])
        print("Temperature (°C):", weather["temperature_c"])
        print("Temperature (°F):", weather["temperature_f"])
        print("Condition:", weather.get("emoji"), weather["condition"])
        print("Humidity:", weather["humidity"], "%")
        print("Wind Speed:", weather["wind_speed"], "mph")
        if weather["alerts"]: 

            for alert in weather["alerts"]:
                print("Headline:", alert["headline"])
                print("Severity:", alert["severity"])
                print("Event:", alert["event"])
        else:
            print("No weather alerts.")    

        print("|----------------------------|")
        print("Forecast for the next", len(weather["forecast"]), "days:")
        for day in weather["forecast"]:
            date = day["date"]
            condition = day["day"]["condition"]["text"]
            emoji = get_weather_emoji(condition)
            max_temp_c = day["day"]["maxtemp_c"]
            min_temp_c = day["day"]["mintemp_c"]
            max_temp_f = day["day"]["maxtemp_f"]
            min_temp_f = day["day"]["mintemp_f"]

            print(f"Date: {date}")
            print(f"Condition: {emoji} {condition}")
            print(f"Max Temp: {max_temp_c}°C / {max_temp_f}°F")
            print(f"Min Temp: {min_temp_c}°C / {min_temp_f}°F")
            print("|----------------------------|")
def ask_for_another_city():
    while True:

        choice = input("Do you want to check the weather for another city and forecast? (yes/no): ").strip().lower()

        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def main():
    while True:
        city = input("Enter the city name: ").strip()
        while not city:
            print("City name cannot be empty.")
            city = input("Enter the city name: ").strip()

        days = input("Enter the number of days to forecast: ").strip()
        while not days.isdigit() or int(days) < 1 or int(days) > 3:
            print("Please enter a valid number of days (1-3).")
            days = input("Enter the number of days to forecast: ").strip()
        

        weather = get_weather(city, days)
        if weather:
            print_weather_report(weather)
            plot_temperature(weather["forecast"])        
        if not ask_for_another_city():
            print("Thank you for using the Weather Report App!")
            break
     
main()


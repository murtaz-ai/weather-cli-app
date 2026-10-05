# Weather CLI App

A Python command-line weather application that uses WeatherAPI to retrieve current weather conditions and forecast information.

## Features

* Current weather information
* Temperature in Celsius and Fahrenheit
* Weather condition
* Humidity
* Wind speed
* Weather alerts
* Weather forecast
* Temperature graph using Matplotlib
* Multiple city searches
* Input validation
* API error handling

## Technologies

* Python
* Requests
* Matplotlib
* python-dotenv
* WeatherAPI

## Setup

1. Clone the repository.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project folder.

4. Add your WeatherAPI key:

```text
WEATHER_API_KEY=your_api_key_here
```

5. Run the application:

```bash
python weather.py
```

## Note

The API key is stored in a `.env` file and is excluded from Git using `.gitignore`.

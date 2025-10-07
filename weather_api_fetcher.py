import requests

API_KEY = 'your_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    city = input("Enter city: ")
    weather = get_weather(city)
    print(weather)

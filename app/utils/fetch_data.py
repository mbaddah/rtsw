import requests

def fetch_solar_wind_data(url):
    response = requests.get(url)
    return response.json()
import requests

def fetch_kyoto_dst():
    # Define the URL for the JSON data
    url = "https://services.swpc.noaa.gov/products/kyoto-dst.json"
    # Fetch the JSON data
    response = requests.get(url, timeout=60)
    return response.json()
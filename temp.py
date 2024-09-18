import requests
import json
from prometheus_client import start_http_server, Gauge

# Define the URL for the JSON data
url = "https://services.swpc.noaa.gov/products/kyoto-dst.json"

# Fetch the JSON data
response = requests.get(url)
data = response.json()

# Define a Prometheus Gauge metric
g = Gauge('kyoto_dst', 'Kyoto Dst Index', ['time'])

# Skip the header row and parse the JSON data to set the metric
for entry in data[1:]:
    time = entry[0]
    value = float(entry[1])
    g.labels(time=time).set(value)

# Start an HTTP server to expose the metrics
start_http_server(8000)

# Keep the script running to serve the metrics
print("Serving metrics on http://localhost:8000")
while True:
    pass
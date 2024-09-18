import requests
import json
from datetime import datetime
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

# Define the URL for the JSON data
url = "https://services.swpc.noaa.gov/products/kyoto-dst.json"

# Fetch the JSON data
response = requests.get(url)
data = response.json()

# Create a registry for the metrics
registry = CollectorRegistry()

# Define a Prometheus Gauge metric with a custom timestamp label
g = Gauge('kyoto_dst', 'Kyoto Dst Index', ['timestamp'], registry=registry)

# Skip the header row and parse the JSON data to set the metric
for entry in data[1:]:
    time_str = entry[0]
    value = float(entry[1])
    
    # Convert time string to a datetime object and then to a Unix timestamp
    time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").timestamp()

    # Set the metric value with the custom timestamp label
    g.labels(timestamp=str(time_obj)).set(value)

# Push the metrics to the Pushgateway
push_to_gateway('localhost:9091', job='kyoto_dst_job', registry=registry)

print("Metrics pushed to Pushgateway")
# RTSW
Real time solar wind observability using Grafana

# Plan

Initial spike work on following:

- Display K-index based on https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json
- Display 2 hour solar wind https://services.swpc.noaa.gov/products/solar-wind/mag-2-hour.json 
- Display dst https://services.swpc.noaa.gov/products/kyoto-dst.json


# Misc notes:

- Verify windows exporter running via http://localhost:9182/metrics
- Add datasource using http://host.docker.internal:9090
- Using https://grafana.com/grafana/dashboards/20763-windows-exporter-dashboard-2024/ 

# References

https://www.swpc.noaa.gov/products/real-time-solar-wind
https://services.swpc.noaa.gov/products/solar-wind/
https://services.swpc.noaa.gov/products/

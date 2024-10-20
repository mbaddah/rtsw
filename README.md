# RTSW
Real time solar wind observability using Grafana

# Plan

Initial spike work on following:

- Display K-index based on https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json
- Display 2 hour solar wind https://services.swpc.noaa.gov/products/solar-wind/mag-2-hour.json 
- Display dst https://services.swpc.noaa.gov/products/kyoto-dst.json


# Mysql setup (old needs updating)

- `init-db.sql` mysql initialisation script.

Configure env variables:

```
- DB_HOST
- DB_USER
- DB_PASSWORD
- DB_NAME
```

<!-- # Misc notes: -->
<!-- - Verify windows exporter running via http://localhost:9182/metrics
- Add datasource using http://host.docker.internal:9090
- Using https://grafana.com/grafana/dashboards/20763-windows-exporter-dashboard-2024/  -->

# To run

- `docker-compose up --build`
- `python rtsw.py` (this will be redundant once setup Dockerfile)

# To-do (initially):

- Load grafana configuration automatically on launch (DB source, dashboard, user setup etc...)
- Save state of MySql / dst_data DB on teardown
- Add tests

# To-do (long-term):

- Update infrastructure to scale accordingly
- Add polling
- 

# References

https://www.swpc.noaa.gov/products/real-time-solar-wind
https://services.swpc.noaa.gov/products/solar-wind/
https://services.swpc.noaa.gov/products/

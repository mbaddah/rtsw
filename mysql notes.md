
# MySQL notes:

### Set environment variables via:

```
setx DB_HOST "localhost"
setx DB_USER "root"
setx DB_PASSWORD "admin"
setx DB_NAME "kyoto_dst"
```

### Launch mysql client via cmd:

`mysql -u your_username -p your_database`

e.g.
`mysql -u root -p`
`mysql -h localhost -u root -p`

To connect to mysql instance within docker network:

`mysql -h host.docker.internal -P 3306 -u root -p`


### Common mysql commands:

`CREATE DATABASE temp_database;`
`SHOW DATABASES;`

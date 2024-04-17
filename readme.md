# Build
docker build --rm -t micro .

# Run
docker run  -v $PWD/:/home -i -t micro /bin/bash

---
# The Config.ini file
It should look like:
```ini
[db]
server =xxx.database.windows.net
database = xxx
username = xxx
password = xxx
```


# Local SQL Server

```sh
sudo docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=BamIh@sapassthign1!!!!20" \
   -p 1433:1433 --name sql1 --hostname sql1 \
   -d \
   mcr.microsoft.com/mssql/server:2022-latest

```


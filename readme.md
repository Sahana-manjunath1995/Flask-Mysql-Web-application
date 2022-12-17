# Netflix project
This is a netflix statistic dashboard. 
Code for creating a docker web application with Flask, MySQL and containerize using docker-compose tutorial

### How to run?
```bash
docker compose  --env-file .env.local up --build
```
### How to stop?
```bash
docker compose  --env-file .env.local.wsl down
```

### mysqldump
mysql -uroot -proot <table_name> > <filename.sql>

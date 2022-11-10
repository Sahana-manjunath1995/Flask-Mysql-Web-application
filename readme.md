# Netflix project
This is a netflix statistic dashboard.

### How to run?
```bash
docker compose  --env-file .env.local up --build
```
### How to stop?
```bash
docker compose  --env-file .env.local down
```

### mysqldump
mysql -uroot -proot <table_name> > <filename.sql>
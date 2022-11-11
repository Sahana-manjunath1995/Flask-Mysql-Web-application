# Netflix project
This is a netflix statistic dashboard.


### How to load csv file data into mysql table?

```
LOAD DATA INFILE 'file_path of local host' INTO TABLE  table_name CHARACTER SET utf8 FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;
```

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

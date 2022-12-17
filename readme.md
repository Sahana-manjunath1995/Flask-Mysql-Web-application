# Netflix project
This is a netflix statistic dashboard. 
Code for creating a docker web application with Flask, MySQL and containerize using docker-compose tutorial

## Requirements

   - Docker
      1. mariadb:latest image
   - Flask
   - mysql.connector
   - HTML
   - css
   - Javascript
   - J-Query
   

## Installation of docker in Ubuntu-wsl

   1. Check if the system is up-to-date using the following command:

      $ sudo apt-get update

   2. Install Docker using the following command:

      $ sudo apt install docker.io

      You’ll then get a prompt asking you to choose between y/n - choose y

   3. Install all the dependency packages using the following command:

      $ sudo snap install docker

   4. Before testing Docker, check the version installed using the following command:

      $ docker --version



## Docker command to create and run the container

    1. docker pull mariadb:latest

    2. docker run --d -p 3306:3306 --network mysql-network -v /var/lib/mysql/data:/var/lib/mysql/data -v /mnt/e/Movies1/movie_oup.csv:/mnt/e/Movies1/movie_oup.csv -v
    /mnt/e/Movies1/director_oup.csv:/mnt/e/Movies1/director_oup.csv -v /mnt/e/Movies1/cast_oup.csv:/mnt/e/Movies1/cast_oup.csv -v
    /mnt/e/Movies1/netflix_movie_title.csv:/mnt/e/Movies1/netflix_movie_title.csv --name mysqldb --env MARIADB_USER=sahana --env MARIADB_PASSWORD=root --env
    MARIADB_ROOT_PASSWORD=root  mariadb:latest



## Login to mysql

  1. Connecting localhost to container in docker using TCP method

     mysql --host=localhost --protocol=TCP -uroot -proot

     or

  2. Start the container and run the following commands

     docker start contaner_name

     docker exec -it contaner_name bash

     mysql -uroot -proot

  3. After login create database named 'College' and insert data into table based on relationship given in data model
  
  
## Module requirements
  
  - import logging
  - from flask import Flask, render_template, jsonify, request
  - import configparser
  - import mysql.connector

## Installation

      pip install -U flask
      
  
      pip install mysql-connector-python
  
## Configuration

  1. Create config.ini file in application folder with the following content in file:
    [mysql]
    host = 'db'
    user = 'root'
    password =  'root'
    database = 'Movies'
    
  2. Create config.py file in  application folder
     refer: ./app
     
 
  


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

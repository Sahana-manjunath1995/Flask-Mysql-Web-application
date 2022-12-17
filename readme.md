# Netflix project
This is a netflix statistic dashboard. 
Code for creating a docker web application with Flask, MySQL and containerize using docker-compose

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
```bash
$ sudo apt-get update
```

   2. Install Docker using the following command:
```bash
$ sudo apt install docker.io
```

      You’ll then get a prompt asking you to choose between y/n - choose y

   3. Install all the dependency packages using the following command:
```bash
$ sudo snap install docker
```

   4. Before testing Docker, check the version installed using the following command:
```bash
$ docker --version
```


## Docker command to create and run the container

    1. docker pull mariadb:latest

    2. docker run --d -p 3306:3306 --network mysql-network -v /var/lib/mysql/data:/var/lib/mysql/data -v /mnt/e/Movies1/movie_oup.csv:/mnt/e/Movies1/movie_oup.csv -v
    /mnt/e/Movies1/director_oup.csv:/mnt/e/Movies1/director_oup.csv -v /mnt/e/Movies1/cast_oup.csv:/mnt/e/Movies1/cast_oup.csv -v
    /mnt/e/Movies1/netflix_movie_title.csv:/mnt/e/Movies1/netflix_movie_title.csv --name mysqldb --env MARIADB_USER=sahana --env MARIADB_PASSWORD=root --env
    MARIADB_ROOT_PASSWORD=root  mariadb:latest



## Login to mysql

  1. Connecting localhost to container in docker using TCP method
```bash
 mysql --host=localhost --protocol=TCP -uroot -proot
```
    or

   Start the container and run the following commands
```bash
docker start contaner_name
```
```bash
docker exec -it container_name bash
```
```bash
mysql -uroot -proot
```

  3. After login create database named 'College' and insert data into table based on relationship given in data model
  
## Folder structure

      .
      ├── app
      │   ├── Dockerfile      
      │   ├── config.ini      
      │   ├── config.py       
      │   ├── netflix1.py     
      │   ├── requirements.txt
      │   └── templates
      │       └── movie.html
      ├── docker-compose.yml
      └── readme.md
      

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
```bash
      [mysql]
      host = 'db'
      user = 'root'
      password =  'root'
      database = 'Movies'
 ```

  2. Create config.py file in  application folder
     refer: ./app
     
## Containerizing the flask application

  1. Create Dockerfile in app folder
      refer : ./app


  2. Create requirement.txt file in app folder for listing all the dependencies
      refer : ./app
      
  3. Create docker-compose.yml file in application root directory.

      refer : application root directory
      
  4. Command for building containers
  ```bash
  docker compose  --env-file .env.local up --build
  ```

  5. Container is created by using Dockerfile

  6. Connection between containers is done using docker-compose.yml
  
## Deploy the application in AWS

   1. Create EC2 instance in AWS
   2. Generate key-pair and download security key file ie .pem file
    
   ### Connect local host to EC2 using ssh comand
   
      1. Open an SSH client
      
      2.Locate the private key file. The key used to launch this instance is dockerflask.pem
      
      3. Change the file permission
   ```bash
   chmod 400 dockerflask.pem
   ```
   
      4. Connect to localhost using EC2 instance Public DNS:
 
  
  ```bash
  ssh -i "dockerflask.pem" ubuntu@ec2-13-232-58-4.ap-south-1.compute.amazonaws.com
  ```
      5. Create project directory in EC2 instance
   
      6. Install Docker using the following command:
  ```bash
  $ sudo apt install docker.io
  ``` 
      7. Install git using the following command:
  ```bash
   $ sudo apt-get install git.
  ```
  
      8. Initialize git by using the below command
  ```bash
  $ git init
  ```

      9. Clone the repository to EC2 instance using http method
  ```bash
  $ git clone https://github.com/Sahana-manjunath1995/netflix_project.git
  ```
   
      10. Run the application using docker compose
  ```bash
  docker compose  --env-file .env.dev up --build
  ```
   
## Extra information
### How to stop?
```bash
docker compose  --env-file .env.local.wsl down
```

### mysqldump
mysql -uroot -proot <table_name> > <filename.sql>

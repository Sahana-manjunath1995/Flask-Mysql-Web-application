import configparser

import mysql.connector

config = configparser.ConfigParser()
config.read('config.ini')

def connect():
    return mysql.connector.connect(host = config['mysql']['host'],
                                   user = config['mysql']['user'],
                                   passwd = config['mysql']['password'],
                                 #    port_no = config['mysql'][port],
                                   db = config['mysql']['database'])



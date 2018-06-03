# -*- coding: utf-8 -*-

import pymysql

MYSQL_DB = 'douban'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
MYSQL_HOST = 'localhost'

connection = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER,
                             password=MYSQL_PASSWD, db=MYSQL_DB,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
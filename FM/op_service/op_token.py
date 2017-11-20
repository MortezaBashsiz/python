import mysql.connector as mariadb
from ConfigParser import *
import re

config = ConfigParser()
config.read('/etc/fm/fm.conf')

def string_parser(string,delimiter):
    _SPLITS = re.split(delimiter,string)
    return _SPLITS

DB_MYSQL = config.get('database','mysql')

DB_STR = string_parser(DB_MYSQL,'@')
DB_STR = string_parser(DB_STR[0],':')
DB_USER = DB_STR[0]
DB_PASS = DB_STR[1]

DB_STR = string_parser(DB_MYSQL,'@')
DB_STR = string_parser(DB_STR[1],':')
DB_HOST = DB_STR[0]
DB_PORT = DB_STR[1]
DB_NAME = DB_STR[2]

def validate_token(token):
    db = mariadb.connect(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME)
    cursor = db.cursor()
    try:
        cursor.execute("""SELECT EXISTS(SELECT token FROM tb_token WHERE token = %s )""", (token,))
        _token_exist = cursor.fetchone()
        if _token_exist[0] > 0:
            result = "success"
        else:
            result = "failed"
    except mariadb.Error as err:
        db.rollback()
        result = "failed"
        print(err)
    db.close()
    return result
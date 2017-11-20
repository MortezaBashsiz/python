
import mysql.connector as mariadb
import re
from ConfigParser import *

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

def insert_peers(source,destination,unique_id):
    db = mariadb.connect(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME)
    cursor = db.cursor()
    try:
        cursor.execute('INSERT INTO tb_peers (source,destination,unique_id)values(%s,%s,%s)',(source,destination,unique_id))
        db.commit()
        result = "success"
    except mariadb.Error as err:
        db.rollback()
        result = "failed"
        print(err)
    db.close()
    return result

def delete_peers(unique_id):
    db = mariadb.connect(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME)
    cursor = db.cursor()
    try:
        cursor.execute("""DELETE FROM tb_peers WHERE unique_id = %s""",(unique_id,))
        db.commit()
        result = "success"
    except mariadb.Error as err:
        db.rollback()
        result = "failed"
        print(err)
    db.close()
    return result
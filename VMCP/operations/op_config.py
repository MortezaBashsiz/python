
from configparser import *
import re

ConfigFilePath="/etc/vmcp/vmcp.conf"

config = ConfigParser()
config.read(ConfigFilePath)

def string_parser(string,delimiter):
    _SPLITS = re.split(delimiter,string)
    return _SPLITS

def mysql_data():
	_mysql_data={}
	DB_MYSQL = config.get('database','mysql')
	
	DB_STR = string_parser(DB_MYSQL,'@')
	DB_STR = string_parser(DB_STR[0],':')
	_mysql_data['user'] = DB_STR[0]
	_mysql_data['pass'] = DB_STR[1]

	DB_STR = string_parser(DB_MYSQL,'@')
	DB_STR = string_parser(DB_STR[1],':')

	_mysql_data['host'] = DB_STR[0]
	_mysql_data['port'] = DB_STR[1]
	_mysql_data['name'] = DB_STR[2]
	
	return _mysql_data

def log_data():
	_log_data={}
	_log_data['path'] = config.get('log','path')
	_log_data['level'] = config.get('log','level')
	return _log_data
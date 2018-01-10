import logging
from . import op_config as conf 

def debug(string):
	_Log_Data = conf.log_data()
	logging.basicConfig(filename=_Log_Data['path'],level=logging.DEBUG,format='%(asctime)s %(levelname)s  %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
	logging.debug(string)

def INFO(string):
	_Log_Data = conf.log_data()
	logging.basicConfig(filename=_Log_Data['path'],level=logging.INFO,format='%(asctime)s %(levelname)s  %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
	logging.debug(string)

def warning(string):
	_Log_Data = conf.log_data()
	logging.basicConfig(filename=_Log_Data['path'],level=logging.warning,format='%(asctime)s %(levelname)s  %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
	logging.debug(string)

def logger(string):
	_Log_Data = conf.log_data()
	if _Log_Data['level'] == 'DEBUG' :
		debug(string)
	elif _Log_Data['level'] == 'INFO' :
		info(string)
	elif _Log_Data['level'] == 'WARNING' :
		warning(string)


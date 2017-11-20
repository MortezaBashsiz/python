import logging
import op_config as conf 

def debug(string):
	_Log_Data = conf.log_data()
	logging.basicConfig(filename=_Log_Data['path'],level=logging.DEBUG)
	logging.debug(string)

def INFO(string):
	_Log_Data = conf.log_data()
	logging.basicConfig(filename=_Log_Data['path'],level=logging.INFO)
	logging.debug(string)

def debug(string):
	_Log_Data = conf.log_data()
	logging.basicConfig(filename=_Log_Data['path'],level=logging.DEBUG)
	logging.debug(string)

def logger(string):
	# _Log_Data = {}
	_Log_Data = conf.log_data()
	if _Log_Data['level'] == 'DEBUG' :
		debug(string)
	elif _Log_Data['level'] == 'INFO' :
		info(string)
	elif _Log_Data['level'] == 'WARNING' :
		warning(string)


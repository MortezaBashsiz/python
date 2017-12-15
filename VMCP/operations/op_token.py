import mysql.connector as mariadb
import uuid 
import datetime
from operations import op_config as conf
from operations import op_logger as log

def generate_uuid():
    return str(uuid.uuid4())

def delete_token(user_id):
    _MysqlData=conf.mysql_data()
    db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
    try:
        cursor = db.cursor()
        _log_message = "TOKEN CONNECTED TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
    except mariadb.Error as err:
        log.logger(str(err))

    try:
        cursor.execute("""DELETE FROM table_tokens WHERE user_id = %s """, (user_id,))
        result = 'true'
        _log_message = "TOKEN DELETED for user_id="+user_id
        log.logger(_log_message)
    except mariadb.Error as err:
        db.rollback()
        result = 'false'
        log.logger(str(err))
    db.close()
    return result

def renew_token(user_id):
    _MysqlData=conf.mysql_data()
    _token=generate_uuid()
    try:
        db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
        cursor = db.cursor()
        _log_message = "RENEW TOKEN CONNECTED TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
        try:
            cursor.execute('UPDATE table_tokens SET token = %s WHERE user_id = %s',(_token,str(user_id)))
            db.commit()
            result = 'true'
            _log_message = "TOKEN RENEW FOR USER user_id="+str(user_id)+" is token="+_token+""
            log.logger(_log_message)
        except mariadb.Error as err:
            db.rollback()
            result = 'false'
            log.logger(err)
    except mariadb.Error as err:
        log.logger(str(err))
        result = 'false'

    db.close()
    return result    

def validate_token(token):
     currentDT = datetime.datetime.now()
    _MysqlData=conf.mysql_data()
    db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
    try:
        cursor = db.cursor()
        _log_message = "VALIDATE TOKEN CONNECTED TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
    except mariadb.Error as err:
        log.logger(str(err))

    try:
        cursor.execute("""SELECT expire_date FROM table_tokens WHERE token = %s """, (token,))
        _token_exist = cursor.fetchone()
        if _token_exist[0] > currentDT:
            result = 'true'
            _log_message = "TOKEN STILL IS VALID token="+token
        else:
            result = 'false'
            _log_message = "TOKEN STILL IS INVALID token="+token
        log.logger(_log_message)
    except mariadb.Error as err:
        db.rollback()
        result = 'false'
        log.logger(str(err))
    db.close()
    return result
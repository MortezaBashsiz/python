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
    currentDT = datetime.datetime.now().replace(microsecond=0)
    expireDT = currentDT + datetime.timedelta(minutes = 10)
    try:
        db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
        cursor = db.cursor()
        _log_message = "RENEW TOKEN CONNECTED TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
        try:
            cursor.execute("""SELECT EXISTS(SELECT id FROM table_tokens WHERE user_id = %s)""",(str(user_id),))
            token_exist = cursor.fetchone()
            if token_exist[0] > 0:
                try:
                    cursor.execute('UPDATE table_tokens SET token = %s  , expire_date = %s WHERE user_id = %s ',(_token,str(expireDT),str(user_id)))
                    db.commit()
                    result = 'true'
                    _log_message = "TOKEN RENEW FOR USER user_id="+str(user_id)+" is token="+_token+"" + " NEW EXPIRE DATE is= " + str(expireDT) + " CURRENT DATE is= " +str(currentDT) 
                    log.logger(_log_message)
                except mariadb.Error as err:
                    db.rollback()
                    result = 'false'
                    log.logger(str(err))
            else:
                try:
                    cursor.execute('INSERT INTO table_tokens (user_id,token,expire_date)values(%s,%s,%s)',(str(user_id),_token,str(expireDT)))
                    db.commit()
                    result = 'true'
                    _log_message = "TOKEN RENEW FOR USER user_id="+str(user_id)+" is token="+_token+""
                    log.logger(_log_message)
                except mariadb.Error as err:
                    db.rollback()
                    result = 'false'
                    log.logger(str(err))
        except mariadb.Error as err:
            log.logger(str(err))
            result = 'false'
    except mariadb.Error as err:
        log.logger(str(err))
        result = 'false'

    db.close()
    return result      

def validate_token(user_id):
    arr_result={}
    _token='FFFF'
    result='false'
    currentDT = datetime.datetime.now().replace(microsecond=0)
    _MysqlData=conf.mysql_data()
    db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
    try:
        cursor = db.cursor()
        _log_message = "VALIDATE TOKEN CONNECTED TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
    except mariadb.Error as err:
        log.logger(str(err))

    try:
        cursor.execute("""SELECT expire_date FROM table_tokens WHERE user_id = %s""", (str(user_id),))
        _token_expire_date = cursor.fetchone()
        if datetime.datetime.strptime(str(_token_expire_date[0]),'%Y-%m-%d %H:%M:%S') > currentDT:
            try:
                cursor.execute("""SELECT token FROM table_tokens WHERE user_id = %s""",(str(user_id),))
                _token = cursor.fetchone()
                result = 'true'
                _log_message = "TOKEN STILL IS VALID token="+" EXPIREDATE=  "+ str(_token_expire_date[0]) + "  CURRENTDATE=  " + str(currentDT)
            except mariadb.Error as err:
                log.logger(str(err))
                result = 'false'
        else:
            result = 'false'
            _log_message = "TOKEN IS NOT VALID token="+str(_token) +" EXPIREDATE=  "+ str(_token_expire_date[0]) + "  CURRENTDATE=  " + str(currentDT)
        log.logger(_log_message)
    except mariadb.Error as err:
        db.rollback()
        result = 'false'
        log.logger(str(err))
    db.close()
    arr_result['result'] = result
    arr_result['token'] = _token[0]
    return arr_result 

def check_token(user_id):
    _MysqlData=conf.mysql_data()
    db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
    cursor = db.cursor()
    try:
        cursor.execute("""SELECT EXISTS(SELECT id FROM table_tokens WHERE user_id = %s)""",(str(user_id),))
        token_exist = cursor.fetchone()
        if token_exist[0] > 0:
            result = 'true'
            _log_message = "TOKEN EXIST FOR USER user_id="+str(user_id)
            log.logger(_log_message)
        else:
            result = 'false'
            _log_message = "TOKEN FOR USER user_id="+str(user_id)+"  DOES NOT EXIST"
            log.logger(_log_message)
    except mariadb.Error as err:
        log.logger(str(err))
        result = 'false'

    return result

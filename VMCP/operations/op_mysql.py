import mysql.connector as mariadb
from operations import op_config as conf
from operations import op_logger as log
from operations import op_token as token
import datetime

def update_user(user_id,ip):
    currentDT = datetime.datetime.now().replace(microsecond=0)
    _MysqlData=conf.mysql_data()
    try:
        db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
        cursor = db.cursor()
        _log_message = "UPDATE USER CONNECTED TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
        try:
            cursor.execute('UPDATE table_users SET last_ip = %s , last_date = %s WHERE id = %s',(str(ip),str(currentDT),user_id))
            db.commit()
            result = 'true'
            _log_message = "USER UPDATED user_id="+str(user_id)+" , last_ip="+ip+" , last_date="+str(currentDT)+""
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

def validate_user(username,password,ip):
    _MysqlData=conf.mysql_data()
    _user_id=0
    arr_result={}
    db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
    try:
        cursor = db.cursor()
        _log_message = "VALIDATE USER TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
    except mariadb.Error as err:
        log.logger(str(err))

    try:
        cursor.execute("""SELECT EXISTS(SELECT id FROM table_users WHERE name = %s AND pass = %s )""", (username,password))
        _user_exist = cursor.fetchone()
        if _user_exist[0] > 0:
            result = 'true'
            cursor.execute("""SELECT id FROM table_users WHERE name = %s AND pass = %s """, (username,password))
            _user_id = cursor.fetchone()
            # token.renew_token(_user_id[0])
            update_user(_user_id[0],ip)
        else:
            result = 'false'
            _log_message = "USER INVALID user="+username
        log.logger(_log_message)
    except mariadb.Error as err:
        db.rollback()
        result = 'false'
        log.logger(str(err))
    db.close()
    if result == 'true':
        arr_result['result'] = result
        arr_result['user_id'] = _user_id[0]
    else:
        arr_result['result'] = result
        arr_result['user_id'] = '0'
    return arr_result

import mysql.connector as mariadb
import op_config as conf
import op_logger as log

def validate_token(token):
    _MysqlData=conf.mysql_data()
    try:
        db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
        cursor = db.cursor()
        _log_message = "CONNECTED TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
    except mariadb.Error , err:
        log.logger(str(err))

    try:
        cursor.execute("""SELECT EXISTS(SELECT token FROM tb_token WHERE token = %s )""", (token,))
        _token_exist = cursor.fetchone()
        if _token_exist[0] > 0:
            result = "success"
            _log_message = "TOKEN VALIDATED token="+token
        else:
            result = "failed"
            _log_message = "TOKEN INVALID token="+token
        log.logger(_log_message)
    except mariadb.Error , err:
        db.rollback()
        result = "failed"
        log.logger(str(err))
    db.close()
    return result
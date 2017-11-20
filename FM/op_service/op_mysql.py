import mysql.connector as mariadb
import op_config as conf
import op_logger as log

def insert_peers(source,destination,unique_id):
    _MysqlData=conf.mysql_data()
    try:
        db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
        cursor = db.cursor()
        _log_message = "CONNECTED TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
    except mariadb.Error , err:
        log.logger(str(err))

    try:
        cursor.execute('INSERT INTO tb_peers (source,destination,unique_id)values(%s,%s,%s)',(source,destination,unique_id))
        db.commit()
        result = "success"
        _log_message = "ROW INSERT INTO DB source="+source+" , destination="+destination+" , unique_id="+unique_id
        log.logger(_log_message)
    except mariadb.Error as err:
        db.rollback()
        result = "failed"
        log.logger(err)
    db.close()
    return result

def delete_peers(unique_id):
    _MysqlData=conf.mysql_data()
    try:
        db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
        cursor = db.cursor()
        _log_message = "CONNECTED TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
    except mariadb.Error , err:
        log.logger(str(err))

    try:
        cursor.execute("""DELETE FROM tb_peers WHERE unique_id = %s""",(unique_id,))
        db.commit()
        result = "success"
        _log_message = "ROW DELETED unique_id="+unique_id
        log.logger(_log_message)
    except mariadb.Error as err:
        db.rollback()
        result = "failed"
        log.logger(err)
    db.close()
    return result
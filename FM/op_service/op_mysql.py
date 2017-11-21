import mysql.connector as mariadb
import op_config as conf
import op_logger as log

def insert_peers(source,destination,unique_id):
    _MysqlData=conf.mysql_data()
    try:
        db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
        cursor = db.cursor()
        _log_message = "INSERT PEER CONNECTED TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
        cursor.execute("""SELECT unique_id FROM tb_peers WHERE source=%s AND destination=%s AND unique_id=%s""",(source,destination,unique_id))
        row = cursor.fetchall()    
        length=int(len(row))
        if length == 0:
            try:
                cursor.execute('INSERT INTO tb_peers (source,destination,unique_id)values(%s,%s,%s)',(source,destination,unique_id))
                db.commit()
                result = 200
                _log_message = "ROW INSERTED INTO DB source="+source+" , destination="+destination+" , unique_id="+unique_id
                log.logger(_log_message)
            except mariadb.Error as err:
                db.rollback()
                result = 551
                log.logger(err)
        elif length > 0 :
            _log_message = "ROW ALREADY EXIST WITH source="+source+" , destination="+destination+" , unique_id="+unique_id
            log.logger(_log_message)
            result = 553
    except mariadb.Error , err:
        log.logger(str(err))
        result = 550

    db.close()
    return result

def delete_peers(unique_id):
    _MysqlData=conf.mysql_data()
    try:
        db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
        cursor = db.cursor()
        _log_message = "DELETE PEER CONNECTED TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
        cursor.execute("""SELECT unique_id FROM tb_peers WHERE unique_id = %s""",(unique_id,))
        row = cursor.fetchall()    
        length=int(len(row))
        if length > 0:
            try:
                cursor.execute("""DELETE FROM tb_peers WHERE unique_id = %s""",(unique_id,))
                db.commit()
                result = 200
                _log_message = "ROW DELETED unique_id="+unique_id
                log.logger(_log_message)
            except mariadb.Error as err:
                db.rollback()
                result = 551
                log.logger(err)
        elif length == 0 :
            _log_message = "ROW DOES NOT EXIST WITH unique_id="+unique_id
            log.logger(_log_message)
            result = 552
    except mariadb.Error , err:
        result = 550
        log.logger(str(err))
    
    db.close()
    return result
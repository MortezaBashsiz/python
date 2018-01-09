import mysql.connector as mariadb
import op_config as conf
import op_logger as log

def insert_cdr(cdr_row):
    _MysqlData=conf.mysql_data()
    try:
        db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
        cursor = db.cursor()
        _log_message = "INSERT CDR CONNECTED TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
        try:
            cursor.execute('INSERT INTO cdr (caller_id_name,caller_id_number,destination_number,context,start_stamp,answer_stamp,end_stamp,duration,billsec,hangup_cause,uuid,bleg_uuid,accountcode,domain_name,server_id)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(cdr_row['caller_id_name'],cdr_row['caller_id_number'],cdr_row['destination_number'],cdr_row['context'],cdr_row['start_stamp'],cdr_row['answer_stamp'],cdr_row['end_stamp'],cdr_row['duration'],cdr_row['billsec'],cdr_row['hangup_cause'],cdr_row['uuid'],cdr_row['bleg_uuid'],cdr_row['accountcode'],cdr_row['domain_name'],cdr_row['server_id']))
            db.commit()
            _log_message = "ROW INSERTED INTO DB  "+cdr_row['caller_id_name']+" , "+cdr_row['caller_id_number']+" , "+cdr_row['destination_number']+" , "+cdr_row['context']+" , "+cdr_row['start_stamp']+" , "+cdr_row['answer_stamp']+" , "+cdr_row['end_stamp']+" , "+cdr_row['duration']+" , "+cdr_row['billsec']+" , "+cdr_row['hangup_cause']+" , "+cdr_row['uuid']+" , "+cdr_row['bleg_uuid']+" , "+cdr_row['accountcode']+" , "+cdr_row['domain_name']+" , "+cdr_row['server_id']
            log.logger(_log_message)
        except mariadb.Error as err:
            db.rollback()
            log.logger(err)
    except mariadb.Error , err:
        log.logger(str(err))
    db.close()
    return result

def get_cdr_last_row():
    _MysqlData=conf.mysql_data()
    _Service_Data=conf.service_data()
    arr_result={}
    db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
    try:
        cursor = db.cursor()
        _log_message = "GET CDR LAST ROW TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
    except mariadb.Error as err:
        log.logger(str(err))
    try:
        cursor.execute("""SELECT * FROM cdr WHERE server_id='%s' ORDER BY id desc limit 1""", (_Service_Data['server_id']))
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
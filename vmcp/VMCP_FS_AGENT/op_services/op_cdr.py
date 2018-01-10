
import mysql.connector as mariadb
import subprocess 
import re

from . import op_config as conf
from . import op_logger as log

def record_pars(record):
    _arr_result={}
    _SPLITS = re.split(',',record)
    _arr_result['caller_id_name']=_SPLITS[0]
    _arr_result['caller_id_number']=_SPLITS[1]
    _arr_result['destination_number']=_SPLITS[2]
    _arr_result['context']=_SPLITS[3]
    _arr_result['start_stamp']=_SPLITS[4]
    _arr_result['answer_stamp']=_SPLITS[5]
    _arr_result['end_stamp']=_SPLITS[6]
    _arr_result['duration']=_SPLITS[7]
    _arr_result['billsec']=_SPLITS[8]
    _arr_result['hangup_cause']=_SPLITS[9]
    _arr_result['uuid']=_SPLITS[10]
    _arr_result['bleg_uuid']=_SPLITS[11]
    _arr_result['accountcode']=_SPLITS[12]
    _arr_result['domain_name']=_SPLITS[13]
    _arr_result['server_id']=_SPLITS[14]
    return _arr_result

def insert_cdr(cdr_row):
    _MysqlData=conf.mysql_data()
    _Service_Data=conf.service_data()
    try:
        db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
        cursor = db.cursor()
        _log_message = "INSERT CDR CONNECTED TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
        try:
            cursor.execute('INSERT INTO cdr (caller_id_name,caller_id_number,destination_number,context,start_stamp,answer_stamp,end_stamp,duration,billsec,hangup_cause,uuid,bleg_uuid,accountcode,domain_name,server_id)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(str(cdr_row['caller_id_name'])[1:-1],str(cdr_row['caller_id_number'])[1:-1],str(cdr_row['destination_number'])[1:-1],str(cdr_row['context'])[1:-1],str(cdr_row['start_stamp'])[1:-1],str(cdr_row['answer_stamp'])[1:-1],str(cdr_row['end_stamp'])[1:-1],str(cdr_row['duration'])[1:-1],str(cdr_row['billsec'])[1:-1],str(cdr_row['hangup_cause'])[1:-1],str(cdr_row['uuid'])[1:-1],str(cdr_row['bleg_uuid'])[1:-1],str(cdr_row['accountcode'])[1:-1],str(cdr_row['domain_name'])[1:-1],_Service_Data['server_id']))
            db.commit()
            _log_message = "ROW INSERTED INTO DB  "+cdr_row['caller_id_name']+" , "+cdr_row['caller_id_number']+" , "+cdr_row['destination_number']+" , "+cdr_row['context']+" , "+cdr_row['start_stamp']+" , "+cdr_row['answer_stamp']+" , "+cdr_row['end_stamp']+" , "+cdr_row['duration']+" , "+cdr_row['billsec']+" , "+cdr_row['hangup_cause']+" , "+cdr_row['uuid']+" , "+cdr_row['bleg_uuid']+" , "+cdr_row['accountcode']+" , "+cdr_row['domain_name']+" , "+cdr_row['server_id']
            log.logger(_log_message)
        except mariadb.Error as err:
            db.rollback()
            log.logger(err)
    except mariadb.Error as err:
        log.logger(str(err))
    db.close()

def get_cdr_last_row_db():
    _MysqlData=conf.mysql_data()
    _Service_Data=conf.service_data()
    _arr_result={}
    db = mariadb.connect(host=_MysqlData['host'],port=_MysqlData['port'],user=_MysqlData['user'],password=_MysqlData['pass'],database=_MysqlData['name'])
    try:
        cursor = db.cursor()
        _log_message = "GET CDR LAST ROW TO MYSQL host="+_MysqlData['host']+" , port="+_MysqlData['port']
        log.logger(_log_message)
    except mariadb.Error as err:
        log.logger(str(err))
    try:
        cursor.execute("""SELECT * FROM cdr WHERE server_id= %s ORDER BY id desc limit 1""", (_Service_Data['server_id'],))
        _last_row = cursor.fetchone()
        _arr_result['caller_id_name']=_last_row[1]
        _arr_result['caller_id_number']=_last_row[2]
        _arr_result['destination_number']=_last_row[3]
        _arr_result['context']=_last_row[4]
        _arr_result['start_stamp']=_last_row[5]
        _arr_result['answer_stamp']=_last_row[6]
        _arr_result['end_stamp']=_last_row[7]
        _arr_result['duration']=_last_row[8]
        _arr_result['billsec']=_last_row[9]
        _arr_result['hangup_cause']=_last_row[10]
        _arr_result['uuid']=_last_row[11]
        _arr_result['bleg_uuid']=_last_row[12]
        _arr_result['accountcode']=_last_row[13]
        _arr_result['domain_name']=_last_row[14]
        _arr_result['server_id']=_last_row[15]
    except mariadb.Error as err:
        db.rollback()
        result = 'false'
        log.logger(str(err))
    db.close()
    return _arr_result

def validate_row(row):
    if row['caller_id_name'] is None :
        row['caller_id_name'] = ""
    if row['caller_id_number'] is None :
        row['caller_id_number'] = ""
    if row['destination_number'] is None :
        row['destination_number'] = ""
    if row['context'] is None :
        row['context'] = ""
    if row['start_stamp'] is None :
        row['start_stamp'] = ""
    if row['answer_stamp'] is None :
        row['answer_stamp'] = ""
    if row['end_stamp'] is None :
        row['end_stamp'] = ""
    if row['duration'] is None :
        row['duration'] = ""
    if row['billsec'] is None :
        row['billsec'] = ""
    if row['hangup_cause'] is None :
        row['hangup_cause'] = ""
    if row['uuid'] is None :
        row['uuid'] = ""
    if row['bleg_uuid'] is None :
        row['bleg_uuid'] = ""
    if row['accountcode'] is None :
        row['accountcode'] = ""
    if row['domain_name'] is None :
        row['domain_name'] = ""
    if row['server_id'] is None :
        row['server_id'] = ""
    return row

def split(deli,string):
    _SPLITS = re.split(deli,string)
    return _SPLITS

def get_cdr_last_row_line_number(row):
    row = validate_row(row)
    _Service_Data = conf.service_data()
    _str_cmd = "grep -n '\""+row['caller_id_name']+"\",\""+str(row['caller_id_number'])+"\",\""+str(row['destination_number'])+"\",\""+str(row['context'])+"\",\""+str(row['start_stamp'])+"\",\""+str(row['answer_stamp'])+"\",\""+str(row['end_stamp'])+"\",\""+str(row['duration'])+"\",\""+str(row['billsec'])+"\",\""+str(row['hangup_cause'])+"\",\""+str(row['uuid'])+"\",\""+str(row['bleg_uuid'])+"\",\""+str(row['accountcode'])+"\",\""+str(row['domain_name'])+"\"' "+_Service_Data['cdr_csv_log_file']+"| awk -F \":\" '{print $1}'"
    _grep_result = subprocess.Popen(_str_cmd,shell=True,stdout=subprocess.PIPE)
    out, err = _grep_result.communicate()
    print (split("\n",str(split('\'',str(out))[1])))
    # print (out)

def insert_from_file_to_db(line_number):
    _counter = 0
    _Service_Data = conf.service_data()
    with open(_Service_Data['cdr_csv_log_file']) as file:
        _counter = 1
        for line in file:
            _counter += 1
            # if _counter >= line_number
            #     if len(line) > 0:
            #         insert_cdr(record_pars(line))


import csv
from freeswitch import *
import mysql.connector as mariadb

def select_peers(number):
    result = '1111'
    db = mariadb.connect(host='192.168.5.30',user='fm_admin',password='123456',database='fm')
    cursor = db.cursor()
    try:
        cursor.execute("""SELECT source,destination FROM tb_peers WHERE source = %s OR destination = %s""",(number,number,))
        row = cursor.fetchall()
        if row :
                source = str(row[0][0])
                destination = str(row[0][1])
                if number == source :
                    result = destination
                elif number == destination :
                        result = source
    except mariadb.Error as err:
        db.rollback()
    db.close()
     
    return result

def handler(session, args):
    caller_num = session.getVariable("caller")
    peer = select_peers(caller_num)
    freeswitch.consoleLog('info', '###################################################################################: %s\n' % peer)
    session.execute("execute_extension", "'{0}' XML default".format(peer))
    session.answer()


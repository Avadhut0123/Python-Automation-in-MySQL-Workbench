import mysql.connector
import os 
from datetime import datetime

class db:
    global CHName,COURIER_NAME,DATE
    CHName = 'Biasket'
    COURIER_NAME = 'B_EXP'
    DATE = now = datetime.now()

    def conn(self):                             #stored crdentials in env file
        db_conn = mysql.connector.connect(
        host=os.environ.get('Mysql_host'),user=os.environ.get('Mysql_User'),passwd=os.environ.get('Mysql_Pass'),database=os.environ.get('Mysql_Database_name'))
        # print(db_conn.is_connected())
        return db_conn
    
    def addChannel_Courier(self):
        db_conn = self.conn()
        cur = db_conn.cursor()

        insert_query = "INSERT INTO channel(name,defaultIdentifier,CreatedBy,CreatedOn)VALUES('"+str(CHName)+"','S','EmizaSupport','"+str(DATE)+"');"
        # print(insert_query)
        cur.execute(insert_query)
        print(cur.rowcount, "Channel inserted") 

        insert_query = "INSERT INTO courier(name,CreatedBy,CreatedOn)VALUES('"+str(COURIER_NAME)+"','EmizaSupport','"+str(DATE)+"');"
        # print(insert_query)
        db_conn = self.conn()
        cur = db_conn.cursor()
        cur.execute(insert_query)
        print(cur.rowcount, "Courier added") # Addition of WH to their respected Users
        db_conn.commit()
 
        db_conn.close() 

a1 = db()
a1.addChannel_Courier()
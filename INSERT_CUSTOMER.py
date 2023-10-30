import mysql.connector
import os 

class db:
    global Name 
    Name = ''
    def conn(self):
        db_conn = mysql.connector.connect(
            host=os.environ.get('Mysql_host'),user=os.environ.get('Mysql_User'),passwd=os.environ.get('Mysql_Pass'),database=os.environ.get('Mysql_Database_name'))
        # print(db_conn.is_connected())
        #stored crdentials in env file
        return db_conn
        
    def insertquery(self):
        create_query = "INSERT INTO customer (`name`,`GroupEmail`,`CreatedBy`,`CreatedOn`)VALUES('AdityA_T','emizasupport@emizainc.com','EmizaSupport',NOW());"
        # select_query = "SELECT * FROM customer;"
        db_conn = self.conn()
        cur = db_conn.cursor()
        cur.execute(create_query)
        db_conn.commit()
 
        print(cur.rowcount, "details inserted")
 
        db_conn.close()  # disconnecting from server
        # data = cur.fetchall()
        # print(data)

a1 = db()
a1.insertquery()


import mysql.connector
import os 

class db:
    global USER_ID,NAME,EMAIL,PASSWORD,WH_NAME
    USER_ID = 'AVIW'
    NAME = 'AVa'
    EMAIL = 'ava@gmail.com'
    WH_NAME = 'Emiza_Welspurn'

    def conn(self):                             #stored crdentials in env file
        db_conn = mysql.connector.connect(
        host=os.environ.get('Mysql_host'),user=os.environ.get('Mysql_User'),passwd=os.environ.get('Mysql_Pass'),database=os.environ.get('Mysql_Database_name'))
        # print(db_conn.is_connected())
        return db_conn
    
    def new_user(self):
        
        db_conn = self.conn()
        cur = db_conn.cursor()

        insert_query = "INSERT INTO users(UserId,Name,Email,Password,CreatedBy,CreatedOn) VALUES ('"+str(USER_ID)+"','"+str(NAME)+"','"+str(EMAIL)+"','yXBAStvuAKZiA1dSQcuQfUKhy+rWNzYc','EmizaSupport',NOW());"
        # print(insert_query)
        cur.execute(insert_query)
        print(cur.rowcount, "User inserted")    #Adding New Users in DB

        WH_ID = "SELECT WarehouseId FROM warehouse WHERE name = '"+WH_NAME+"'"
        cur.execute(WH_ID)
        data4 = cur.fetchall()
        ID = data4[0][0]                        #Getting the WH ID    

        insert_query = "INSERT INTO userwarehouse (UserId,WarehouseId,CreatedBy,CreatedOn) VALUES ('"+str(USER_ID)+"','"+str(ID)+"','EmizaSupport',NOW());"
        # print(insert_query)
        db_conn = self.conn()
        cur = db_conn.cursor()
        cur.execute(insert_query)
        print(cur.rowcount, "WH added to the new User") # Addition of WH to their respected Users
        db_conn.commit()
 
        db_conn.close() 

a1 = db()
a1.new_user()
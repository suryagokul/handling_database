''' 

https://dev.mysql.com/downloads/    from this download workbench (450mb) and installer.. then
pip install mysql-connector-python  which is an api to connect db.

'''

import mysql.connector

conn = mysql.connector.connect(host="localhost",
			user="root",
			password="root")


# conn returns mysql connection object
if conn:
    print("Connection Established")
else:
    print("Connection not Established. please check...")
    

conn.close()    
import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='root',password='raw_pswd',
                                database='drugs_1db')

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:    # if name or pass wrong it handle
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:   # if there is no db exists it handles.
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
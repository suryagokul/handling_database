# 3rd way of establishing conn using dictionaries

from mysql.connector import (connection)

config = {'host': "localhost",
	  'user': "root",
	  'password': "root"
	}

conn = connection.MySQLConnection(**config) # passing as keyword args

print(conn)

conn.close()
from mysql.connector import (connection)

config = {'host': "localhost",
	  'user': "root",
	  'password': "root",
	  'database':'drugs1_db'
	}

conn = connection.MySQLConnection(**config)

cursor = conn.cursor()
query = "SHOW TABLES"
cursor.execute(query) # returns all the tables in 'drugs1_db' db which already exists.

print(*cursor,sep="\n")
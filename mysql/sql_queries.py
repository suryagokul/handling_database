from mysql.connector import (connection)

config = {'host': "localhost",
	  'user': "root",
	  'password': "root",
	  'database':'drugs1_db'
	}

conn = connection.MySQLConnection(**config)

cursor = conn.cursor()

query = "SELECT * FROM vocabulary"  # returns all records in a vocabulary table in drugs1_db database

cursor.execute(query) 

print(*cursor,sep="\n")
from mysql.connector import (connection)

config = {'host': "localhost",
	  'user': "root",
	  'password': "root"
	}

conn = connection.MySQLConnection(**config)

cursor = conn.cursor()
cursor.execute("SHOW DATABASES")

print(cursor)  # returns the query SHOW DATABASES as o/p

for x in cursor:
    print(x)          # returns all databases exists


# or we can easily print using  print(*cursor, sep="\n")

conn.close()
cursor.close()


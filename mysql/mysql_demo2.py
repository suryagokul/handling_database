# 2nd way to establish connection

from mysql.connector import (connection)

conn = connection.MySQLConnection(host="localhost",
				user="root",
				password="root")
print(conn)

conn.close()
import cx_Oracle


conn = cx_Oracle.connect('surya/surya@localhost')

cursor = conn.cursor()

query = 'create table iris_oracle(petal_length number,\
                                  petal_width number,sepal_length number,sepal_width number)'


cursor.execute(query)

print("Table Created Successfully")

cursor.close()
conn.close()

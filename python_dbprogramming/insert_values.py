import cx_Oracle


conn = cx_Oracle.connect('surya/surya@localhost')

cursor = conn.cursor()

#query = 'insert into iris_oracle values(10,20,30,40)' we can also insert multiple rows as below

query = 'insert into iris_oracle values(:petal_length,:petal_width,:sepal_length,:sepal_width)'

records = [(10,20,30,40), (50,60,70,80),(15,24,54,90)]


cursor.executemany(query,records)          #executemany is used for inserting multiple rows at a time
conn.commit()

print("Inserted values Successfully")

cursor.close()
conn.close()

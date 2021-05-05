import cx_Oracle


conn = cx_Oracle.connect('surya/surya@localhost')

cursor = conn.cursor()

try:    

    query = 'select * from iris_oracle'


    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    for row in all_rows:

        print(row)

except cx_Oracle.DatabaseError as e:
    if conn:
        conn.rollback()
        print("there is a problem",e)

finally:
    if cursor:
    
        cursor.close()
    if conn:
        conn.close()

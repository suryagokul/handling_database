import cx_Oracle


conn = cx_Oracle.connect('surya/surya@localhost')

cursor = conn.cursor()

try:    

    query = 'update iris_oracle set petal_length=%d where petal_length<=%d'


    cursor.execute(query %(500,10))         
    conn.commit()

    print("Records Updated Successfully")

except cx_Oracle.DatabaseError as e:
    if conn:
        conn.rollback()
        print("there is a problem",e)

finally:
    if cursor:
    
        cursor.close()
    if conn:
        conn.close()

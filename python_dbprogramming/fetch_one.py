import cx_Oracle


# username/password/@localmachine
conn = cx_Oracle.connect('surya/surya@localhost')

cursor = conn.cursor()

try:    

    query = 'select * from iris_oracle'


    cursor.execute(query)
    row = cursor.fetchone()
    conn.commit()
    while row:

        print(row)
        row = cursor.fetchone()
        

except cx_Oracle.DatabaseError as e:
    if conn:
        conn.rollback()                # if any exception happens it gets rollback(undo) the operation
        print("there is a problem",e)

finally:
    # closing all the resources...
    if cursor:
    
        cursor.close()
    if conn:
        conn.close()

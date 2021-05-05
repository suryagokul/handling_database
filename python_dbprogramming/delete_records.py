import cx_Oracle


conn = cx_Oracle.connect('surya/surya@localhost')

cursor = conn.cursor()

try:
    cutoff_for_petlen = int(input("enter cutoff for petal length > "))
        

    query = 'delete from iris_oracle where petal_length>%d'


    cursor.execute(query %cutoff_for_petlen)         
    conn.commit()

    print("Records deleted Successfully")

except cx_Oracle.DatabaseError as e:
    if conn:
        conn.rollback()
        print("there is a problem",e)

finally:
    if cursor:
    
        cursor.close()
    if conn:
        conn.close()

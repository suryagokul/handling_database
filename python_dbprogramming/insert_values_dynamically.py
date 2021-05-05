import cx_Oracle



conn = cx_Oracle.connect('surya/surya@localhost')

cursor = conn.cursor()

while True:
    petal_length = int(input("enter petal length > "))
    petal_width = int(input("enter petal width > "))
    sepal_length = int(input("enter sepal length > "))
    sepal_width = int(input("enter sepal width > "))

    option = input("If u want to insert another record (Y/N) ")
    if option=='N':
        break
    

query = 'insert into iris_oracle values(%d,%d,%d,%d)'


cursor.execute(query %(petal_length,petal_width,sepal_length,sepal_width))         
conn.commit()

print("Inserted values Successfully")

cursor.close()
conn.close()

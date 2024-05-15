import sqlite3

## Connect to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor obj to insert

cursor=connection.cursor()

## Create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25));

"""

cursor.execute(table_info)

## Insert some more records

cursor.execute('''Insert into STUDENT values('Samyak','Data Science','A')''')
cursor.execute('''Insert into STUDENT values('Sudhansh','Data Science','A')''')
cursor.execute('''Insert into STUDENT values('Shreyas','DEVOPS','B')''')
cursor.execute('''Insert into STUDENT values('Vikas','DEVOPS','B')''')
cursor.execute('''Insert into STUDENT values('Dipesh','Data Science','A')''')


## Display all the records

print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
connection.commit()
connection.close()
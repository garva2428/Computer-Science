import sqlite3

db_connection=sqlite3.connect('business.db')
#cursor object
cursor = db_connection.cursor()

addData = '''
insert into customers (first_name,last_name,phone,country) values (?,?,?,?)
'''

cursor.execute(addData,('John','Doe','052 092 4118','Switzerland'))
db_connection.commit()

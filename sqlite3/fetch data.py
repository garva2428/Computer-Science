import sqlite3

db_connection=sqlite3.connect('business.db')
#cursor object
cursor = db_connection.cursor()

fetchData ='''
select first_name,country from customers
'''

cursor.execute(fetchData)
data=cursor.fetchall()
print(data[0][0])

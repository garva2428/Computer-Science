import sqlite3
from data_analytics import calc_average

connect_to_db=sqlite3.connect('iris.db')
#cursor object
db_cursor = connect_to_db.cursor()

get_data_from_db = '''
select sepal_length from irisData;
'''

db_cursor.execute(get_data_from_db)
data = db_cursor.fetchall()
list1=[]
for data_point in data:
    list1.append(data_point[0])
print(list1)
average_sepal_length = calc_average(list1)
print(f'The average sepal length is: {average_sepal_length}')

db_cursor.close()
connect_to_db.close()
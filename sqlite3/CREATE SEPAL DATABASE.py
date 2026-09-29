import sqlite3

connect_to_db=sqlite3.connect('iris.db')
#cursor object
db_cursor = connect_to_db.cursor()

createTable = '''create table if not exists irisData(
sepal_id INTEGER PRIMARY KEY AUTOINCREMENT,
sepal_length REAL NOT NULL,
sepal_width REAL NOT NULL,
petal_length REAL NOT NULL,
petal_width REAL NOT NULL,
class INTEGER NOT NULL
) STRICT
'''

db_cursor.execute(createTable)
connect_to_db.commit()
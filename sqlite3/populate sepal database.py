import sqlite3

connect_to_db=sqlite3.connect('iris.db')
#cursor object
db_cursor = connect_to_db.cursor()

addData='''
insert into irisData (sepal_length,sepal_width,petal_length,petal_width,class)
values (?,?,?,?,?);
'''

f=open('Iris - all-numbers.csv','r')
headerLine = f.readline()
for line in f:#\n
    line = line.strip () # removes the \n
    line= line.split (',')#creates a list - split on 'comma'
    line = tuple(line)
    
    db_cursor.execute(addData,line)
    connect_to_db.commit()
#close connections    
db_cursor.close()
connect_to_db.close()


    
    

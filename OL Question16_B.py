# Question 16(b)
# Name and School: Garva Ahuja and Athlone Community College

flight_number=['122','125','132','135','155']
direct=[]
indirect=[]
for i in flight_number:
    if i[-1]=='2':
        direct.append(i)
    else:
        indirect.append(i)
        
print('Direct:',direct)
print('Indirect:',indirect)

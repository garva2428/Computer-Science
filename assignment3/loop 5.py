#Author Garva Ahuja
#Date 8/9/25
#Programme Set a variable called total to 0. Ask the user to enter five numbers. After eachinput ask if they wish to add that number to the total. If they do, add the numberelse do not add the number. When they have entered five numbers, display the total.


total=0

for i in range(5):
    n_1=int(input('Number: '))  
    ask=input('Do you want to add this to the total? ')
    
if ask=='yes'or ask=='YES'or ask=='Yes':
    total+n_1
    total+=n_1
else:
    pass
print(total)
    
        
        


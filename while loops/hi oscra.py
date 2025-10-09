#Author Garva Ahuja
#Date 2/10/2025
#Programme Write a program that takes integers from the user and returns the average. Use a while loop and make an empty string the stop criteria.

n=10
counter=0
total=0
while n!='':
    n=input('Enter an integer')
    if n.isdigit():
        n=int(n)
        
        counter+=1
        total+=int(n)
    else:
        pass

print(total/counter)
    

    

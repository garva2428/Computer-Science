#Date 23/10/25
#Author Garva Ahuja
#Programme Write a program which asks the user to enter a string of digits, and a step size.

string=input('Enter a string of digits: ')
stepsize=int(input('Enter a step size: '))
total=0
b=string[0::stepsize]
for i in b:
    b=int(b)
    i=int(i)
    total+=i
    
print(total)




    
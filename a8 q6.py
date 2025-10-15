#Author Garva Ahuja
#Date 14/10/2025
#Programme  Write a Python program to print every integer between 1 and n divisible by m. Also report whether the
#number that is divisible by m is even or odd.

n=input('Enter a number for n:')
m=int(input('Enter a number for m: '))
number=0
n=int(n)

for i in range (1,n+1):
    i=int(i)
    if i%m==0 and i%2==0:
        print(i,'even')
    elif i%m==0 and i%2!=0:
        print(i,'odd')
    
    

            

    


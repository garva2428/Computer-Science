#Author Garva Ahuja
#Date 6/10/2025
#Programme Write a program to check if a number is an Armstrong number. An Armstrong
#number is a number equal to the sum of the cube of it’s digits.

number=0
hello=0
count=0
while number==0:
    n=input('Enter a number: ')
    for i in n:
        n=int(n)
        i=int(i)
        count+=i**3
    break
if count==n:
    print('The number you have entered is an Armstrong number')
else:
    print('The number is not an Armstrong number')
        
    
    
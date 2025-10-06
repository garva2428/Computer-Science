#Author Garva Ahuja
#Date 3/10/2025
#Programme Write a program which takes in a numbers from the user. It should continue taking in numbers until the total of all the numbers entered is greater than 50.

n=10
count=0
total=0
while n>0:
    number=int(input('Enter a number: '))
    count+=1
    total+=number
    if total>50:
        break
    else:
        continue
    

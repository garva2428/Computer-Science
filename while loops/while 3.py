#Author Garva Ahuja
#Date 3/10/2025
#Programme Write a program that takes an integer number and outputs all the even numbers starting from 0 to the number

number=int(input('Enter a number: '))

while number>=0:
    #if number>=0:
        for i in range(0,number+1,2):
           print(i)
        else:
            break

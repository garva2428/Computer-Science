#Author Garva Ahuja
#Date 6/10/2025
#Programme Write a program which asks the user to enter a number between 10 and 20
#inclusive. If they enter a number less than 10, print ‘too low’. If they enter a number
#greater than 20 print ‘too high’. The program should continue until they enter a value
#between 10 and 20 then display the message ‘Thank you’

number=0

while number==0:
    n=int(input('Enter a number: '))
    if 10>n:
        print('Too low')
    elif n>20:
        print('Too high')
    else:
        break

print('Thank you')
    

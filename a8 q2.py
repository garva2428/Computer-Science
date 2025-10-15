#Author Garva Ahuja
#Date 9/10/2025
#Programme Write a program to take N (N > 20) as an input from the user. Print numbers from 11 to N. When the
#number is a multiple of 3, print "Tipsy", when it is a multiple of 7, print "Topsy". When it is a multiple
#of both, print "TipsyTopsy".

n=int(input('Enter a number greater than 20: '))
for i in range (11,n+1):
    if i%3==0 and i%7!=0:
        print('Tipsy')
    elif i%7==0 and i%3!=0:
        print('Topsy')
    elif i%21==0:
        print('TipsyTopsy')
    else:
        print(i)
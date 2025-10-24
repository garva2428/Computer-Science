#Date 23/10/25
#Author Garva Ahuja
#Programme Write a program to check if a string is a palindrome. A palindrome is a word or string
#that reads the same backwards and forwards. For example: racecar; rotator

string=input('Enter a string: ')
if string==string[::-1]:
    print('The string is a palindrome')
else:
    print('The string is not a palindrome')
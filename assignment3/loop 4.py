#Author Garva Ahuja
#Date 8/9/25
#Programme Ask the user to enter their name and a number. Display each letter of their name on a separate line and repeat this for the number of times they entered.

name= input('Name: ')
number= int(input('Number: '))

for i in range(number):
    for letter in name:
        print(letter)
    
            

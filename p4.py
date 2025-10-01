#Author Garva Ahuja
#Date 4th September 2025
#Programme Ask the user to enter three numbers. Add together the first two and store this answer in a variable. Then multiply this result by the third. Display the answer as: The answer is: <calculated result>

n_1=int(input('Enter a number: '))
n_2=int(input('Enter another number: '))
n_3=int(input('Enter another number: '))

add=n_1+n_2
multiply=add*n_3
print('The answer is:',multiply)
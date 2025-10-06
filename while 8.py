#Author Garva Ahuja
#Date 6/10/2025
#Programme Write a program which asks the user to guess a value you have set in your code. The
#program should tell them if their guess is too high or too low and print a well done
#message when they guess it correct telling them how many attempts it took.

value=41
count=0
while value==41:
    guess=int(input('Guess the value: '))
    count+=1
    if guess>value:
        print('Too high')
    elif guess<value:
        print('Too low')
    else:
        break
    
print('Well done')
print('It took you',count,'attempts to guess the value')

    
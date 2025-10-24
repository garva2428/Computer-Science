#Date 23/10/25
#Author Garva Ahuja
#Programme Write a program which asks the user to guess a number between 1 and 100
#inclusive. You can hardcode the number they are trying to guess. Prompt the user if they
#are too high or too low. They can have no more than 7 attempts. If they use more then 7
#print ‘Game Over’ and tell them the answer.

count=0
number=55
allowed=7

    
for i in range(1,8):
    answer=int(input('Guess the number between 1 to 100 inclusive: '))
    count+=1
    if answer==number:
         print('Well done')
         break
    elif count==7:
        print('Game Over')
        print('The answer is 56')
        break



    

    

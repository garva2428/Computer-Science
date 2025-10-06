#Author Garva Ahuja
#Date 3/10/2025
#Programme Write a program that prints from 1 to n squared using a while loop. It should stop the while loop if the iteration count is 50. (Hint use break)

number=int(input('Enter a number: '))
count=0
square=number*2

while square>0:
        count+=1
        print(count**2)
        if count==50:
            break
        elif count==number:
            break
                
        

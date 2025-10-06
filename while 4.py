#Author Garva Ahuja
#Date 3/10/2025
#Programme Write a program that prints from 1 to n using a while loop, it should skip every multiple of 5. (Hint, use % and continue)

number=int(input('Enter a number: '))

while number>=0:
    for i in range(1,number+1):
        if i%5!=0:
            print(i)
            continue
    else:
        break
            
            

    
        
        
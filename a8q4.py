#Author Garva Ahuja
#Date 10/10/2025
#Programme Write a program to input N numbers and then print the second largest number.

number=0
count=0
maximum=-1
second_maximum=maximum


while number==0:
    n=int(input('Enter a number'))
    count+=1
    if maximum<n:
        second_maximum=maximum
        maximum=n
    elif second_maximum<n  and n != maximum:
        second_maximum=n
    
    if count==5:
        break
    else:
        continue
    
print(second_maximum)


        
        
    
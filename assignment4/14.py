#Author Garva Ahuja
#Date 10/9/25
#Programme Print the sum of all the odd numbers from 1 to a given number
number=int(input('Number: '))
total=0

for i in range(1,number+1):
    if i%2==1:
        total=total+i
        print(total)
    else:
        pass


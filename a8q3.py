#Author Garva Ahuja
#Date 9/10/2025
#Programme Write a short program to find largest number of a list of numbers entered through keyboard

number=0
count=0
max=-1

while number==0:
    n=int(input('Enter a number: '))
    count+=1
    if n>max:
        max=n
    if count==5:
        break
    else:
        continue

#final=max(n)
print(max)


    
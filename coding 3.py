#Author Garva Ahuja
#Date 7/10/2025
#Programme Write a program to convert Binary to Decimal

binary=input('Enter a binary number: ')
count=0
final=0

for i in binary:
    binary=int(binary)
    i=int(i)
    final+=i*2**count
    count+=1
    
print(final)
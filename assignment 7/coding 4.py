#Author Garva Ahuja
#Date 7/10/2025
#Programme Write a program to convert decimal to binary

string=''
denary=input('Enter a denary number: ')
number=0
while number==0:
    denary=int(denary)
    quotient=denary//2
    remainder=denary%2
    if quotient!=0:
        string=string+str(remainder)
        continue
    break
print(string)
    

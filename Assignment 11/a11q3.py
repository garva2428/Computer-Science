#Date 23/10/25
#Author Garva Ahuja
#Programme Write a program to take in a string which is a mixture of characters. Extract all the
#digits from the string and print their total.

string=input('Enter a string: ')
total=0
for i in string:
    if i.isdigit()==True:
        i=int(i)
        total+=i
    
print(total)
    
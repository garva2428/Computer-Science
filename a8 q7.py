#Author Garva Ahuja
#Date 14/10/2025
#Programme Write Python programs to sum the given sequences: assignment 8 last question part b

n=input('Enter a number: ')
n=int(n)
total=0

for i in range (1,n+1,2):
    total+=i**2

print(total)

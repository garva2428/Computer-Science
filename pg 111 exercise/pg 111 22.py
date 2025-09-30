#19/9/25
#Name Garva Ahuja
#Programme the sum of n given numbers

n=int(input('Enter the amount of numbers: '))
total=0

for i in range(1,n+1):
    number=int(input('Number: '))
    total+=number

print(total)


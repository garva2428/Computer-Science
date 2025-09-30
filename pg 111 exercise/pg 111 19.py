#19/9/25
#Name Garva Ahuja
#Programme accept numbers till the user enters 0 and find their average

total=0
number=1
count=0
while number!=0:
    number=int(input('Enter a number: '))
    total+=number
    count+=1
print(total/count)

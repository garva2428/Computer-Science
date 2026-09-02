#Garva Ahuja
#linear search
#2/9/26

list1=eval(input('Enter a list: '))
x=int(input('Enter an element: '))
count=0
for i in list1:
    count+=1
    if i==x:
        print(list1.index(x))
        break
    if count==len(list1):
        print('-1')

        
        
    
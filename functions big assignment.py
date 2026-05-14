def range_of_values(a):
    smallest=a[0]
    largest=0
    for i in a:
        if i>largest:
            largest=i
        elif i<smallest:
            smallest=i
    result=largest-smallest
    return result
def average(a):
    result=sum(a)/len(a)
    return result
def median(a):
    n=len(a)
    if n%2==1:
        result=a[(n-1)//2]
    else:
        numerator=a[(n-2)//2]+a[(n-2)//2 + 1]
        result=numerator/2
    return result
def mode(a):
    count=0
    result=0
    for i in a:
        if a.count(i)>result:
            count=a.count(i)
            result=i
    return result
def frequency(a):
    search=[]
    result=''
    for i in a:
        if i not in search:
            result+=f"{i} appears {a.count(i)} times\n"
            search.append(i)
    return result
        
list1=eval(input('Enter a list of numbers: '))
check=range_of_values(list1)
check2=average(list1)
check3=median(list1)
check4=mode(list1)
check5=frequency(list1)
print(check)
print(check2)
print(check3)
print(check4)
print(check5)



            


        
    
    

#LINEAR SEARCH

def binarysearch(list1,target):
    list1.sort()
    low=list1.index(list1[0])
    high=list1.index(list1[-1])
    middle=high+low//2
    
    while list1[middle] != target:
        middle=high+low//2
        
        if list1[middle]==target:
            return middle
        
        else:
            if list1[middle]>target:
                high=middle - 1
            if high<low:
                return -1
            
            else:
                if list1[middle]<target:
                    low=middle + 1
                if low>high:
                    return -1
                
list1=eval(input('Enter a list: '))
target=int(input('Set a target: '))
hello=binarysearch(list1,target)
print(hello)
                
            
    
    
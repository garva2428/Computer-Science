#bubble sort
n=0

def bubble_sort(list1):
    while n==0:
        check=list1.sort()
        
        for i in list1:
            pos=list1.index(i)
            if i>list1[pos+1]:
                a=list1.pop(pos)
                list1.insert(pos+1,a)
                list1.insert(pos,i)
            if check==list1:
                break
            
            
        return list1

list1=[10,8,6,4,2]
hello=bubble_sort(list1)
print(hello)
#yet to finish
            
            
    
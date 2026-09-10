#simple sort
def simple_sort(a,b):
    while len(a)!=0:
        for i in a:
            a.remove(i)
            if len(b)!=0 and i>b[-1]:
                b.insert(len(b),i)
            elif len(b)!=0 and i<b[0]:
                b.insert(0,i)
            elif len(b)==0:
                b.append(i)
            else:
                for char in b:
                    if char>i:
                        b.insert(b.index(char),i)
            
    return b

a=eval(input('Enter a list: '))
b=[]
hello=simple_sort(a,b)
print(hello)
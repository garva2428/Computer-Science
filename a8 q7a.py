#Author Garva Ahuja
#Date 14/10/2025
#Programme Write Python programs to sum the given sequences: assignment 8 last question part a

number=0
positive=2/9
negative=-5/13
a=2
b=9
c=5
d=13

while number==0:
    
    for i in range(1,7,2):
        positive+=((a+6)/(b+8))
        a+=6
        b+=8
    for i in range(2,7,2):
        negative+=(((c+6)/(d+8))*(-1))
        c+=6
        d+=8
        
    break
        
print(positive+negative)


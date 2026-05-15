#functions assignment 3
#Garva Ahuja
#exercise 2

choice=int(input('Enter 1 for Encrytption, 2 for Decryption: '))
message=input('Enter the message: ')
key=int(input('Enter the key: '))

def encrypt(a,b):
    a=a.upper()
    result=''
    for i in a:
        if i.isalpha():
            index=ord(i)
            find=index+b
            if find>90:
                find=find-25
            add=chr(find)
            result+=add
        else:
            result+=i
    return result
def decrypt(c,d):
    c=c.upper()
    result=''
    for char in c:
        if char.isalpha():
            index=ord(char)
            find=index-d+25
            add=chr(find)
            result+=add
        else:
            result+=char
    return result
if choice==1:
    check=encrypt(message,key)
    print(check)
if choice==2:
    check1=decrypt(message,key)
    print(check1)
    
    
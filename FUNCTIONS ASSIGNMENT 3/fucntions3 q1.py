#functions assignment 3
#Garva Ahuja
#exercise 1

alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def encrypt(a,b):
    a=a.upper()
    result=''
    for i in a:
        if i.isalpha():
            add=alphabets.index(i)
            hello=(add+b)%26
            result+=(alphabets[hello])
        else:
            result+=i
    return result
def decrypt(c,d):
    c=c.upper()
    result=''
    for char in c:
        if char.isalpha():
            add=alphabets.index(char)
            hello2=(add-d)%26
            result+=(alphabets[hello2])
        else:
            result+=char
    return result
choice=int(input('If you want to encrypt the message enter 1, else if you want to decrypt the message enter 2: '))
message=input('Enter a message: ')
key=int(input('Enter the key: '))
if choice==1:
    check1=encrypt(message,key)
    print(check1)
if choice==2:
    check2=decrypt(message,key)
    print(check2)



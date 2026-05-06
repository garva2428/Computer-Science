#Question 16(b)
#Name and School: Garva Ahuja

sentence=input('Enter a sentence: ')
words=1
vowels=0
for i in sentence:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowels+=1
    if i==' ':
        words+=1
print(f'''The sentence "{sentence}" contains:
{words} words
{vowels} vowels''')


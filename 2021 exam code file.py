# Question 16(a)
# Examination Number: Garva Ahuja

# function definition used in part (v)
def is_anagram(w1, w2):
    a1=w1.lower()
    a2=w2.lower()
    if sorted(a1) == sorted(a2):
        return w1+" is an anagram of "+w2
    else:
        return w1+" is not an anagram of "+w2
        

word1 = input("Enter the first word: ")
word2 = input('Enter the second word: ')
hello=is_anagram(word1,word2)
print(hello)


# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams

c1=word1.lower()
c2=word2.lower()
if (sorted(c1) == sorted(c2)):
    print(word1,'is an anagram of',word2)
else:
    print(word1,'is not an anagram of',word2)
    
phrase=input('Enter a phrase: ')
p1=phrase.lower()
compare=''
for i in p1:
    if i!=' ':
        compare+=i
        
if sorted(compare)==sorted(c1):
    print(word1,'is an anagram of',phrase)
else:
    print(word1,'is not an anagram of',phrase)
if sorted(compare)==sorted(c2):
    print(word2,'is an anagram of',phrase)
else:
    print(word2,'is not an anagram of',phrase)


    
    
        
    
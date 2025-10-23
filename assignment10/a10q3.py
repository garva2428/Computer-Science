#Date 21/10/25
#Author Garva Ahuja
#Proramme For this question you may need to use indexing, slicing and the replace() method.
#Create a string from a given string where all occurrences of its first char have been
#changed to '$', except the first char itself.]

string=input('Enter a string: ')
a=string[1:]
c=string[0]
b=a.replace(string[0],'$')
print(c+b)


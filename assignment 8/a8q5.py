#Author Garva Ahuja
#Date 10/10/2025
#Programme Write a complete Python program to do the following:
#(i) read an integer Х. (ii) determine the number of digits n in X.
#(iii) form an integer Y that has the number of digits n at ten's place and the most significant digit of X
#at one's place. (iv) Output Y.

x=input('Enter a number:')
y=len(x)

for i in x:
    i=int(i)
    print(y*10+i)
    break


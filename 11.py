#Author Garva Ahuja
#Date 3rd September 2025
#Programme Write a program to compute simple interest and compound interest.



principal=int(input('Enter the principal: '))
rate= float(input('What is the interest rate? '))
time= int(input('How many years is the course of repayment? '))

simple=principal*(1+rate/100*time)
compound=principal*(1+rate/100)**time
          
          
print('If your interest is simple, your final amount is',simple,'.If your interest is compound, your final amount is',compound,'.')
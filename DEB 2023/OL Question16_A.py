# Question 16 (a)
# Name and School: Garva Ahuja and Athlone Community College

flight_num=input('Enter your flight number: ')
destination=input('Enter your destination:')
num_ppl=int(input('Enter the number of people in your travle group:'))
children=int(input('Enter the number of children in the travel group:'))
print('Your flight number is',flight_num)
print('You are travelling to',destination)
print('There are',num_ppl,'people in the travel group')
if flight_num.upper()=='EI125':
    print('The cost of your flights is \u20ac',520*num_ppl-50*children)
elif flight_num.upper()=='EI121':
    print('The cost of your flights is \u20ac',400*num_ppl-50*children)
    

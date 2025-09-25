#for loops are used to iterate over a sequence
#a string or range of numbers

#to looop through the numbers 1-5
for i in range(6):
    print(i, end= ',')
    
for letter in 'apple':
    print(letter)
    
fruit=input('Enter a fruit: ')
for letter in fruit:
    for i in range(3):
        print(letter)
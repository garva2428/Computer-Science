#Author Garva Ahuja
#Date 2nd September 2025
#Programme Wriet a short program that asks for your height in centimetres and then converts your height to feet and inches.

height=int(input('What is your height in cm?'))
inches= height/2.54
print(inches)
feet= inches//12
remainder= inches%12

print('Your height in feet and inches is',feet,'feet and',remainder,'inches.')

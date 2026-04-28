#Question 16(a)
#Name and School Garva Ahuja

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius=(5/9)*fahrenheit-32
    return celsius

choice=input('Enter 1 for Celsius to Fahrenheit conversion or 2 for Fahrenheit to Celsius conversion: ')
if choice=='1': #conditional
    celsius = float(input('Enter the temperature in Celsius: '))
    ctof=round(celsius_to_fahrenheit(celsius),2)
    kelvin=round(celsius+273.15,2)
    print(celsius, chr(176)+"C is equal to",ctof,chr(176)+"F and",kelvin,'K')

elif choice=='2': #conditional
    fahrenheit=float(input('Enter the temperature in Fahrenheit: '))
    ftoc=round(fahrenheit_to_celsius(fahrenheit),2)
    kelvin=ftoc+273.15
    print(fahrenheit,chr(176)+'F is equal to',ftoc,chr(176)+'C','and',kelvin,'K')
    


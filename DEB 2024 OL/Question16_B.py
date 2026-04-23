# Question 16(a)
# Name and School: Garva Ahuja

principal=int(input('Enter the principal investment amount: €'))
interest=float(input('Enter the annual interest rate (e.g. 0.05 for 5% interest): '))
value=principal
for i in range(1,11):
    value+=(interest*value)
    end=str(round(value,2))
    print('Year',i,'- Investment value: €'+end)  

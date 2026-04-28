#Question 16(b)
#Name and School Garva Ahuja

temperatures=[14,23.5,72,56,45.5]
hello=0
ogmean=round((sum(temperatures)/len(temperatures)),2)
while hello==0:
    enter=float(input('Enter a temperature: '))
    temperatures.append(enter)
    minimum=min(temperatures)
    maximum=max(temperatures)
    print('Maximum temperature =',maximum,'Minimum temperature =',minimum)
    mean=round((sum(temperatures)/len(temperatures)),2)
    print('Mean temperature =',mean)
    if mean>ogmean:
        print('The mean temperature is increasing')
        ogmean=mean
    elif mean<ogmean:
        print('The mean temperature is decreasing')
        ogmean=mean
        
        


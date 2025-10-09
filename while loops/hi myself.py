#Author Garva Ahuja
#Date 2/10/2025
#Programme Write a program that takes test grades from the user and returns their average and the letter grade of the average. Use a while loop and make negative number the stop criteria. A >=90 B 80-89 C 70-79 D 60-69 F 59 or less


subjects=0
avg=0
no=int(input('How many subjects do you do? '))
count=0


while no>0:
    grade=int(input('What was your grade? '))
    avg+=grade
    count+=1
    no=no-1
    
avg_1=avg/count
print(avg_1)



if avg_1>=90:
    print('Your average grade is A',avg_1)
elif 80<=avg_1<90:
    print('Your average grade is B',avg_1)
elif 70<=avg_1<80:
    print('Your average grade is C',avg_1)
elif 60<=avg_1<70:
    print('Your average grade is D',avg_1)
elif avg_1<60:
    print('Your average grade is F',avg_1)

else:
    pass

    

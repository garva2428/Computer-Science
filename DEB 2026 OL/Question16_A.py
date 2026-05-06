# Question 16(a)
# Name and School: Garva Ahuja

books = []
num = int(input("How many books have you read?"))
for i in range(0,num):
    book=input("Enter the title of the book you've read: ")
    books.append(book)
if num>=3:
    print("Fantastic! You've read",num,"books - keep reading!")
print('Book(s) read: ')
for g in books:
    print(g)

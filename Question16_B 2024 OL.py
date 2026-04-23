#Please enter name: Garva Ahuja

from datetime import datetime

prompt = input("Please enter prompt:")

if prompt.__contains__("hello".lower()):
    print("Hi there, how are you?")
elif prompt.__contains__("name".lower()):
    print("My name is ExamBot, how can I help?")
elif prompt.__contains__("time".lower()):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
elif prompt.__contains__('weather'.lower()):
    print('It is always sunny in Ireland')
else:
    print('I am sorry, I do not know that one?')
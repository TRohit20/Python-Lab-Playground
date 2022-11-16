# Task: Develop a program to take input from user for goal and dealine

import datetime

user_input = input("Enter your goal and deadline: \n")
input_list = user_input.split(':')

goal = input_list[0]
deadline = input_list[1]

# Convert string to dates
deadline_date = datetime.datetime.strptime(deadline, "%d/%m/%Y")

print(input_list)
print(datetime.datetime.strptime(deadline, "%d/%m/%Y"))

# How many days or hours remaining till the deadline?
today_date = datetime.datetime.today()

time_left = deadline_date - today_date
print(f'The amount of time left to {goal} until your deadline is {time_left}')

hours_left = int(time_left.total_seconds() / 60 / 60)
print(f'The amount of time left to {goal} until your deadline is {hours_left}')


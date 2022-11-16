print("Python Data types")

print(1)  # Integer

print(3.5)  # Float

print(str(3.4) + ' is a float data type ')

print(f'an example of float can be {3.4}')

print((20 + 10) * 2)

cal_units = 24 * 60 * 60
name_of_unit = "seconds"
print(f'20 days are {20 * cal_units} {name_of_unit}')
print(f'30 days are {30 * cal_units} {name_of_unit}')
print(f'40 days are {40 * cal_units} {name_of_unit}')
print(f'45 days are {45 * cal_units} {name_of_unit}')
days = 20


def first_function(days, custom_text):
    print('Hey this is a sample function')
    var = "it's a variable inside function "
    print(f'Sample arithmetic:{days} days are {days * cal_units} {name_of_unit} {custom_text}')
    # print(custom_text)
    print(var)


def test():
    try:
        num1 = input("Enter a number: \n")
        num2 = input("Enter another number: \n")
        sm = int(num1) + int(num2)  # or print
        print(sm)
    except ValueError:
        print('invalid input, Please enter a number')


test()


def days_to_units(days):
    return f'{days} days are {days * cal_units} {name_of_unit}'


def validate_user_input():
    # if u_ip.isdigit():
    try:
        user_input_number = int(days_element)  # Casting
        if user_input_number > 0:
            cal_value = days_to_units(user_input_number)
            print(cal_value)
        elif user_input_number == 0:
            print('You have entered 0. Enter a positive value')
        else:
            print('Please enter a valid positive integer')
# except: is also fine, it is generic so will catch and handle all errors
    except ValueError:
        print("Input is not a program. Enter a integer")


u_ip = ""
while u_ip != "exit":
    u_ip = input("Hey user, enter number of days as a comma separated list and I will convert it to hours count: \n")
    list_of_days = u_ip.split(",")
    print(type(list_of_days))
    print(type(list_of_days))

    print(set(list_of_days))
    print(type(set(list_of_days)))

    for days_element in set(list_of_days):
        validate_user_input()

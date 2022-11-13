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
    num1 = input("Enter a number: \n")
    num2 = input("Enter another number: \n")
    return int(num1) + int(num2)  # or print


ans = test()
print(ans)


def days_to_units(days):

    if days > 0:
        return f'{days} days are {days * cal_units} {name_of_unit}'
    elif days == 0:
        print('You have entered 0. Enter a positive value')
    else:
        print('You have entered invalid input')


u_ip = input("Hey user, enter number of days and I will convert it to hours count: \n")

if u_ip.isdigit():
    user_input_number = int(u_ip)  # Casting
    cal_value = days_to_units(user_input_number)
    print(cal_value)
else:
    print("Input is not a program. Enter a integer")


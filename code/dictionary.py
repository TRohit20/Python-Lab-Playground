user_input = input("Hey, Please enter number of days and conversion unit: \n ")
days_and_units = user_input.split(":")

# Accessing elements of a list and storing them in dictionary
days_and_units_dict = {"days": days_and_units[0], "units": days_and_units[1]}
print(days_and_units_dict)


# Function to convert the given days to units
def units_conversion(days, conversion_unit):
    if conversion_unit == "hours":
        return f"{days} days are {days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{days} days are {days * 24 *60} in minutes"
    else:
        print("Sorry, the given is unsupported unit")


def validate_then_execute():
    try:
        # Accessing a value using the key
        # user_input_v = int(days_and_units_dict["days"])
        # Accessing using .get() method
        user_input_v = int(days_and_units_dict.get("days"))
        if user_input_v > 0:
            calculated_value = units_conversion(user_input_v, days_and_units_dict["units"])
            print(calculated_value)
        elif user_input_v == 0:
            print("You entered 0 which is not a valid input as the conversion would be 0 anyways")
        else:
            print("You entered a negative number! Please enter a positive number")
    except:
        print("The given input is not a integer")


validate_then_execute()
print(type(days_and_units_dict))

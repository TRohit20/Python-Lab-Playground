input_prompt = "Enter number of days and unit to be converted to: \n"


def units_conversion(days, conversion_unit):
    if conversion_unit == "hours":
        return f"{days} days are {days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{days} days are {days * 24 *60} in minutes"
    else:
        print("Sorry, the given is unsupported unit")


def validate_and_execute(days_and_units_dict):
    try:
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

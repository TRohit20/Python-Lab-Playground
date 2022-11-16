from helper import validate_and_execute, input_prompt
# import helper

user_input = ""
while user_input != "end":
    user_input = input(input_prompt)
    days_and_units = user_input.split(":")
    days_and_units_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    # helper.validate_and_execute(days_and_units_dictionary)
    validate_and_execute(days_and_units_dictionary)

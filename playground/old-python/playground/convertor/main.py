# basic list operations
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute() -> object:
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculation_value = days_to_units(user_input_number)
            print(calculation_value)
        elif user_input_number == 0:
            print("invalid data - put more then 0")
        else:
            print("Invalid data - put positive a number")
    except ValueError:
        print("Invalid datatype put a number - ValueError")



user_input = ""
while user_input != "exit":
    user_input = input("Welcome! To know how meny hours in a amount of days, put a number.\n")
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()
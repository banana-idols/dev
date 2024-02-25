"""
# concatenation
print('20 days are ' + str(20 * 24 * 60) + ' minutes')
print(f'20 days are {20 * 24 * 60} minutes')

# variables
calculation_to_units = 24 * 60 * 60
name_of_unit = "seconds"
name_of_unit_1 = "hours"

print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
print(f"35 days are {30 * calculation_to_units} {name_of_unit}")
print(f"50 days are {50 * calculation_to_units} {name_of_unit}")
print(f"110 days are {110 * calculation_to_units} {name_of_unit}")


# function
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days): # parametr
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")


days_to_units(35)  # parametr



# scope
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def scope_check(num_of_days):
    print(name_of_unit)
    print(num_of_days)


scope_check(2)



# user input interaction starts here
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    # returning result to function (in case, user input)
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


user_input = input("To Start Converting Units Type in Data.\n")
user_input_number = int(user_input)

calculation_value = days_to_units(user_input_number)

print(calculation_value)


# conditionals (if/els) boolean data type
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculation_value = days_to_units(user_input_number)
            print(calculation_value)
        elif user_input_number == 0:
            print("invalid data - put more then 0")
        else:
            print("Invalid data - put a number")
    except ValueError:
        print("Invalid datatype put a number - ValueError")


user_input = input("To Start Converting Units Type in Data.\n")
validate_and_execute()

# while loop
calculation_to_units = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute() -> object:
    try:
        user_input_number = int(user_input)
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
    user_input = input("To Start Converting Units Type in Data.\n")
    validate_and_execute()


# lists and for loop
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

"""

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
# Unit converter by @rdhudson
# Completed as part of a GCSE computer science course

import time
import os
import sys
import re

# Function to clear the console
def clear_console():
    if os.name == 'nt':  
        # For Windows
        os.system('cls')
    else:  
        # For macOS and Linux
        os.system('clear')

clear_console()

# Welcome message
print("\nUNIT CONVERTER BY @rdhudson\n")
print("Avalible units to convert to and from:\n\nb\nB\nKB\nMB\nGB\nTB\n")

# Unit directory
unit = {
    "b": 1,
    "B": 8,
    "KB": 1000,
    "MB": 1000**2,
    "GB": 1000**3,
    "TB": 1000**4,
    "PB": 1000**5
}

# Function to restart the program
def restart_program():
    print("Action not recognized\nRestarting Program...")
    time.sleep(5)
    os.execl(sys.executable, sys.executable, *sys.argv)

# Function to ask if the user wants to quit or run another calculation
def ask_to_continue():
    choice = input("\nDo you want to quit the scrpit or run another calculation?\n(q to quit / any other key to restart): ")
    if choice.lower() == 'q':
        print("Quitting the script...")
        time.sleep(3)
        sys.exit()
    else:
        print("\nRestarting the script...")
        time.sleep(3)
        os.execl(sys.executable, sys.executable, *sys.argv)

# Asks user for input, if not a valid unit, restarts program
from_unit = input("Enter the unit you'd like to convert from: ")
print()

operation_from = unit.get(from_unit)

if operation_from:
    to_unit = input("Enter the unit you'd like to convert to: ")
    print()
    operation_to = unit.get(to_unit)

    if operation_to:

        # Function to validate numerical input and restart program if not valid
        def is_valid_number(value):
            return bool(
                re.match(r'^\d{1,3}(,\d{3})*$', value) or re.match(r'^\d+$', value))

        value = input("Enter the value you'd like to convert: ")
        print()

        if is_valid_number(value):
            value = value.replace(',', '')
            value = int(value)
        else:
            restart_program()

        # Function to convert inputted from_unit to bytes
        def convert_to_bytes(value, from_unit):
            return value * unit[from_unit]

        # Function to convert bytes to the inputted to_unit
        def convert_from_bytes(bytes_value, to_unit):
            return bytes_value / unit[to_unit]

        # Converts the value to bytes
        bytes_value = convert_to_bytes(value, from_unit)

        # Converts bytes to the inputted unit
        converted_value = convert_from_bytes(bytes_value, to_unit)

        # Checks if the converted value is in exponential form and checks if input is correct
        if "e" in str(converted_value):
            choice = input("The result is in exponential form. Do you want to convert it to standard form? (y/n): ")
            print()
            if choice.lower() == 'y':
                converted_value = "{:.2f}".format(converted_value)
            elif choice.lower() != 'n':
                restart_program()

        # Prints the output
        print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")

        # Asks if the user wants to run the script again or quit
        ask_to_continue()

    else:
        restart_program()

else:
    restart_program()
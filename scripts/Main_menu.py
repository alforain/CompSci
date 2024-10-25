# Created by @alforian
# This script is the main menu for the GCSE Computer Science Scripts Repository

import re
import os
import sys
import time

# Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# Restarts the program
def invalid_input(parent_function):
    print("Action not recognized\nRestarting Program...")
    time.sleep(5)
    parent_function()

# Asks user if they want to contine, quit or go back to the main menu
def ask_to_continue(parent_function):
    choice = input("\nDo you want to quit the script or run another script?\n(q to quit / r to go back to the main menu / any other key to restart the function): ")
    if choice == 'q':
        print("Quitting the script...")
        time.sleep(2)
        sys.exit()
    elif choice == 'r':
        print("\nGoing back to the main menu...")
        time.sleep(2)
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        time.sleep(2)
        cls()
        parent_function()

# Calculator function
def calculator():
    
    # Sets the current function as a function to be called by ask_to_continue()
    def current_func():
        calculator()
    
    # Asks user for input and replaces 'x' with '*' to allow for multiplication
    print("\nPlease use standard python notation")
    expression = input("Enter expression (e.g., (77-22)/2): ").replace('x', '*')
    
    # Checks user input, evaluates the expression and prints the result
    def is_valid_expression(expression):
        pattern = r'^\s*[\d\(\)]+(\.\d+)?\s*([+\-*/]\s*[\d\(\)]+(\.\d+)?\s*)*$'
        return re.match(pattern, expression) is not None   
    if is_valid_expression(expression):
        try:
            print(eval(expression))
        except Exception as e:
            print(f"Error evaluating expression: {e}")
            invalid_input(current_func)
        ask_to_continue(current_func)
    else:
        invalid_input(current_func)

# Factorial finder function
def factorial_finder():
    
    # Sets the current function as a function to be called by ask_to_continue()
    def current_func():
        factorial_finder()
    
    # Breaks down the factorial calculation into a recursive function
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    # Function to validate user input
    def is_valid_number(value):
        return value.isdigit() and int(value) >= 0

    value = input("\nEnter a non-negative integer to find its factorial: ")

    # Checks if the input is a valid number and if it is, converts it to an integer and calculates the factorial
    if is_valid_number(value):
        value = int(value)
        result = factorial(value)
        print(f"The factorial of {value} is {result}")
    else:
        invalid_input(current_func)
    
    ask_to_continue(current_func)

# Unit converter function
def unit_converter():
    
    # Sets the current function as a function to be called by ask_to_continue()
    def current_func():
        unit_converter()
    
    # Prints and sets available units
    print("Available units to convert to and from:\n\nb\nB\nKB\nMB\nGB\nTB\n")
    unit = {"b": 1, "B": 8, "KB": 1000, "MB": 1000**2, "GB": 1000**3, "TB": 1000**4, "PB": 1000**5}
    
    # Asks user for input, if not a valid unit, restarts program
    from_unit = input("Enter the unit you'd like to convert from: ")
    operation_from = unit.get(from_unit)
    if operation_from:
        to_unit = input("Enter the unit you'd like to convert to:\n")
        operation_to = unit.get(to_unit)

        if operation_to:
            def is_valid_number(value):
                return bool(re.match(r'^\d{1,3}(,\d{3})*$', value) or re.match(r'^\d+$', value))

            value = input("Enter the value you'd like to convert:\n")
            
            # Allows user to input commas in numbers by replacng them with an empty string and converting the value to an integer.
            if is_valid_number(value):
                value = value.replace(',', '')
                value = int(value)
            else:
                invalid_input(current_func)

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
                if choice() == 'y':
                    converted_value = "{:.2f}".format(converted_value)
                elif choice() != 'n':
                    invalid_input(current_func)

            print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")
            
            ask_to_continue(current_func)
        else:
            invalid_input(current_func)
    else:
        invalid_input(current_func)
    
# Main menu
def main_menu():
    def current_func():
        main_menu()
        
    # Checks user input and runs the corresponding function
    print("Welcome to my GCSE Computer Science Scripts Repository!\nAll of the code in this script can be found individually in the scripts folder.\n")
    user_choice = input("Please select a script to run:\n1. Calculator\n2. Factorial Finder\n3. Unit Converter\n4. Exit\n\nEnter: ")
    if user_choice == '1':
        calculator()
    elif user_choice == '2':
        factorial_finder()
    elif user_choice == '3':
        unit_converter()
    elif user_choice == '4':
        print("Exiting the script...")
        time.sleep(3)
        sys.exit()
    else:
        invalid_input(current_func)

main_menu()
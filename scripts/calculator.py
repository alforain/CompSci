# Basic Calculator by @rdhudson
# Completed as part of a GCSE computer science course

import re
import os
import time
import sys

# Welcome message
print("\nCALCULATOR BY @rdhudson\n\nPlease use standard python notation\n")

# Restart program and is used when user input isn't valid
def restart_program():
    print("Action not recognized\nRestarting Program...")
    time.sleep(5)
    os.execl(sys.executable, sys.executable, *sys.argv)

# Asks user if they want to restart the script
def ask_to_continue():
    choice = input("\nDo you want to quit the script or run another calculation?\n(q to quit / any other key to restart): ")
    if choice.lower() == 'q':
        print("Quitting the script...")
        time.sleep(3)
        sys.exit()
    else:
        print("\nRestarting the script...")
        time.sleep(3)
        os.execl(sys.executable, sys.executable, *sys.argv)

# Checks if the value inputted is a number or not
def is_valid_expression(expression):
    pattern = r'^\s*[\d\(\)]+(\.\d+)?\s*([+\-*/]\s*[\d\(\)]+(\.\d+)?\s*)*$'
    return re.match(pattern, expression) is not None

# The actual program
def calculator():
    expression = input("Enter expression (e.g., (77-22)/2): ").replace('x', '*')
    if is_valid_expression(expression):
        try:
            print(eval(expression))
        except Exception as e:
            print(f"Error evaluating expression: {e}")
            restart_program()
        ask_to_continue()
    else:
        restart_program()

calculator()
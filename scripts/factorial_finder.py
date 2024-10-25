# Factorial finder by @alforain
# Completed as part of a GCSE computer science course

import time
import os
import sys

# Clears the console
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:  
        os.system('clear')

clear_console()

# Welcome message
print("\nFACTORIAL FINDER BY @rdhudson\n")

# Restarts the program
def restart_program():
    print("Action not recognized\nRestarting Program...")
    time.sleep(5)
    os.execl(sys.executable, sys.executable, *sys.argv)

# Asks if the user wants to quit or run another calculation
def ask_to_continue():
    choice = input("\nDo you want to quit the script or run another calculation?\n(q to quit / any other key to restart): ")
    if choice() == 'q':
        print("Quitting the script...")
        time.sleep(3)
        sys.exit()
    else:
        print("\nRestarting the script...")
        time.sleep(3)
        os.execl(sys.executable, sys.executable, *sys.argv)

# Calculate factorials
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Validates numerical input and restart program if not valid
def is_valid_number(value):
    return value.isdigit() and int(value) >= 0

# The actual program
value = input("Enter a non-negative integer to find its factorial: ")
print()

if is_valid_number(value):
    value = int(value)
    result = factorial(value)
    print(f"The factorial of {value} is {result}")
else:
    restart_program()

# Asks if the user wants to run the script again or quit
ask_to_continue()
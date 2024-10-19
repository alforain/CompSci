# Marker by @rdhudson
# Completed as part of a GCSE computer science course

import os
import sys
import time

# Clears the console
def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')
clear_console()

# Restarts the program
def restart_program():
    print("\nValue is above 100%\nRestarting Program...")
    time.sleep(2)
    os.execl(sys.executable, sys.executable, *sys.argv)

# Welcome message
print("\nMARKER BY @rdhudson\n")

# User input
x = input("What is your mark?:\n")

# Checks to see if number is valid
def is_number(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


# The actual program
def eval_score(x):
    if not is_number(x):
        restart_program()
    elif int(x) > 100:
        restart_program()    
    elif int(x) >= 90:
        print("\nDistinction")
    elif int(x) >= 70:
        print("\nMerit")
    elif int(x) >= 50:
        print("\nPass")
    else:
        print("\nFail")

eval_score(x)
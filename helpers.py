from consts import *


# ==========================
#
# CHOICE HELPERS
#
def valid_menu_choice(choice):
    try:
        choice = int(choice)
    except ValueError:  # not an int
        return False
    
    for menu_choice in LIST_MENU_CHOICES:
        if int(menu_choice[1]) == choice:
            return True
    return False

def get_choice_by_num(num):
    try:
        num = int(num)
    except ValueError:  # not an int
        return None
    
    for menu_choice in LIST_MENU_CHOICES:
        if int(menu_choice[1]) == num:
            return menu_choice
    return None


# ==========================
#
# PRINT FUNCTIONS
#
def print_line_break(long=False):
    line = "================================"
    if long:
        line += line
    print("")
    print(line)
    print("")
    
def print_menu():
    print_line_break()
    print("Choices:")
    for menu_choice in LIST_MENU_CHOICES:
        print("=\t" + str(menu_choice[1]) + ". " + str(menu_choice[0]))
    print_line_break()
    
# 
# get_menu_choice
# @[RETURN]
# int
#   > 0     - menu choice selected
#   < 0     - invalid menu choice selected
#
def get_menu_choice():
    print_menu()    
    choice = input("Choice >> ")
    if not valid_menu_choice(choice):
        print("\nERR: invalid choice. Please try again.\n")
        return -1
    return int(choice)
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
def print_line_break():
    print("================================")
    
def print_menu():
    print_line_break()
    print("=")
    print("= Search by:")
    for menu_choice in LIST_MENU_CHOICES:
        print("= " + str(menu_choice[1]) + ".\t" + str(menu_choice[0]))
    print("= ")
    print_line_break()
    print("")
    
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
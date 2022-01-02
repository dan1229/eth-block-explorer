import os

from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# ==========================
#
# CONSTS
#
MENU_CHOICE_INVALID = -1
MENU_CHOICE_EXIT = 99
MENU_CHOICE_1 = 1
MENU_CHOICE_2 = 2
MENU_CHOICE_3 = 3
LIST_MENU_CHOICES = [
    ("Latest", MENU_CHOICE_1),
    ("By Address", MENU_CHOICE_2),
    ("By Username", MENU_CHOICE_3),
    ("Exit", MENU_CHOICE_EXIT),
]


# ==========================
#
# HELPERS
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


'''
# ================================================================================== #
# MAIN ============================================================================= #
# ================================================================================== #
'''

w3 = Web3(Web3.HTTPProvider(os.environ.get('INFURA_URL')))

print("========================================================")
print("")
print("**")
print("Welcome to ETH Block Explorer!")
print("**")
print("")

run = True
while run:
    choice = get_menu_choice()

    if choice == MENU_CHOICE_INVALID:  # INVALID choice selection
        pass
    else:
        # EXIT
        if choice == MENU_CHOICE_EXIT:
            run = False
            print_line_break()
            print("\nThank you for using ETH Block Explorer!\n")
            print_line_break()
        else:  # everything else
            print_line_break()
            menu_choice = get_choice_by_num(choice)
            print("\n**\nYOU CHOSE SEARCH " + str(menu_choice[0]) + "\n**\n")
            print_line_break()
            # TODO call corresponding function

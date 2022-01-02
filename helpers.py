from .consts import *


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
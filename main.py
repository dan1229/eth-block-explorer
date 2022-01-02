import os

from web3 import Web3
from dotenv import load_dotenv


from consts import *
from helpers import *

load_dotenv()


def handle_choice(web3, choice):
    if choice == MENU_CHOICE_LATEST:
        block = web3.eth.get_block('latest')
    elif choice == MENU_CHOICE_ADDRESS:
        address = input("Address >> ")
        block = web3.eth.get_block(address)
    elif choice == MENU_CHOICE_USERNAME:
        pass
    else:  # default
        print("INVALID CHOICE...? this shouldnt happen...")
        return
    print(str(block.__dict__))

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
            handle_choice(w3, choice)

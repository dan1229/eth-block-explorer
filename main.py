import os

from web3 import Web3
from dotenv import load_dotenv


from consts import *
from helpers import *

load_dotenv()


def handle_choice(web3, choice):
    if choice == MENU_CHOICE_LATEST:
        block = web3.eth.get_block('latest')
        print(str(block.__dict__))
    elif choice == MENU_CHOICE_ADDRESS:
        address = input("Address >> ")
        block = web3.eth.get_block(address)
        print(str(block.__dict__))
    elif choice == MENU_CHOICE_ACCOUNT_BALANCE:
        account = input("Account >> ")
        balance = web3.eth.get_balance(account)
        print("\n**\nBalance\n" + str(balance) + " ETH\n**\n")
    else:  # default
        print("INVALID CHOICE...? this shouldnt happen...")

'''
# ================================================================================== #
# MAIN ============================================================================= #
# ================================================================================== #
'''

# setup web3
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
            menu_choice = get_choice_by_num(choice)
            print("\n**\nYOU CHOSE " + str(menu_choice[0]) + "\n**\n")
            handle_choice(w3, choice)

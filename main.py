import os

from web3 import Web3, EthereumTesterProvider
from dotenv import load_dotenv


from consts import *
from helpers import *

load_dotenv()


def handle_choice(web3, choice):
    try:
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
            print("THIS SHOULD NOT HAPPEN - YOUR CHOICE CONFIG IS INVALID")
            raise Exception
    except Exception:
        print("INVALID CHOICE?")

'''
# ================================================================================== #
# MAIN ============================================================================= #
# ================================================================================== #
'''

print_line_break(long=True)

# ask network to use
valid = False
network_choice = 1  # main net by default
while not valid:
    print("Which network do you want to use?")
    print("\t1. MainNet (Infura)")
    print("\t2. TestNet")
    network_choice = input("Choice >> ")
    try:
        network_choice = int(network_choice)
        if network_choice != 1 and network_choice != 2:
            raise ValueError
        else:
            valid = True
    except ValueError:
        print("\nInvalid choice. Please try again.\n")

# setup web3
print("Starting web3...")
if network_choice == 1:  # Main Net
    w3 = Web3(Web3.HTTPProvider(os.environ.get('INFURA_URL')))
    print("\tTestNet:\tFalse")
    print("\tProvider URL:\t" + str(os.environ.get('INFURA_URL')))
else:  # Test Net
    w3 = Web3(EthereumTesterProvider())
    print("\tTestNet:\tTrue")
    print("\tProvider URL:\tN/A")

connected = w3.isConnected()

print("\tConnected:\t" + str(connected))


# welcome message
print_line_break(long=True)
print("**")
print("Welcome to ETH Block Explorer!")
print("**")


# menu loop
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

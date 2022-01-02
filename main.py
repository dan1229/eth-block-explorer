import os

from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# ==========================
#
# CONSTS
#
# TODO


# ==========================
#
# PRINT FUNCTIONS
#
def print_line_break():
    print("================================")
    
def print_menu():
    print_line_break()
    print("= 1.")
    print("= 2.")
    print("= 3.")
    print("= ")

def get_menu_choice():
    print_menu()    
    choice = input("= Option >> ")


'''
# ================================================================================== #
# MAIN ============================================================================= #
# ================================================================================== #
'''

w3 = Web3(Web3.HTTPProvider(os.environ.get('INFURA_URL')))

print("========================================================")
print("**")
print("Welcome to ETH Block Explorer!")
print("**")
print("")

run = True
while run:
    get_menu_choice()
import os

from web3 import Web3
from dotenv import load_dotenv

load_dotenv()


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
    print("")
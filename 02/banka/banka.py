# Nasimulujte bankovní systém
#
# V adresáři jsou soubory pojmenované číslem účtu obsahující zůstatek účtu
# Implementujte skript banka.py, který bude ovládán parametry:
#
# Částka se bude čerpat z účtu 111 pomocí --from 111
# Částka se bude připisovat na účet 222 pomocí --to 222
# Převod částky 1000 se určí parametrem --amount 1000
#
# Snažte se řešit různé chyby:
# * účet neexistuje
# * zůstatek by šel do záporu
#
# Příklad použití:
#
#   python banka.py --from 111 --to 222 --amount 1000
#
# V praxi se píší skripty, kde nezáleží na pořadí pojmenovaných parametrů, tj.
# ideální je, když funguje libovolné pořadí parametrů při spuštění:
#
#   python banka.py --from 111 --amount 1000 --to 222
#   python banka.py --amount 1000 --from 111 --to 222
#
# Pro tento pokročilý způsob je však třeba použít pokročilou knihovnu pro práci
# s parametry příkazové řádky, jako např. argparse nebo click.

import sys


def get_acc_balance(path_to_account: str):
    """reads available capital on bank account

    Args:
        path_to_account (str): account name as path

    Returns:
        (float): available money on account
    """
    try:
        with open(path_to_account, "r") as account:
            return float(account.read())
    except FileNotFoundError:
        exit(f"Transfer cancelled, account {path_to_account} does not exist")


def set_new_acc_balance(path_to_account: str, new_balance: float):
    """overwrites means on the back account

    Args:
        path_to_account (str): takes account name as path
        new_balance (float): updated amount available on account
    """
    with open(path_to_account, "w") as account:
        account.write(str(new_balance))


from_param_name = "--from"
to_param_name = "--to"
amount_param_name = "--amount"

# get all terminal params
transaction_order = sys.argv[:]

# check for existence of correctly named params
if (len(transaction_order) != 7
   or from_param_name not in transaction_order
   or to_param_name not in transaction_order
   or amount_param_name not in transaction_order):
    exit(f"Usage: {sys.argv[0]} --from <sender_account> --to <recipient_account> --amount <transferred_amount>")

# figure position of each param
from_index = transaction_order.index(from_param_name) + 1
to_index = transaction_order.index(to_param_name) + 1
amount_index = transaction_order.index(amount_param_name) + 1

# get account numbers and transferred amount
sender_acc_no = transaction_order[from_index]
recipient_acc_no = transaction_order[to_index]
try:
    amount_transferred = float(transaction_order[amount_index])
except ValueError:
    exit("Transferred amount not valid number")

# transfers from to same account illegal
if sender_acc_no == recipient_acc_no:
    exit("Own transfers not allowed")

# check for burglars
if amount_transferred < 0:
    exit("Trying to steal money?")

# get ballance from both accounts
sender_original_balance = get_acc_balance(f"02/banka/{sender_acc_no}")
recipient_original_balance = get_acc_balance(f"02/banka/{recipient_acc_no}")

# check for sufficient account balance
if sender_original_balance - amount_transferred < 0:
    exit(f"Transaction denied! No sufficient funds on account {sender_acc_no}")

# set new account balance
set_new_acc_balance(f"02/banka/{sender_acc_no}", sender_original_balance - amount_transferred)
set_new_acc_balance(f"02/banka/{recipient_acc_no}", recipient_original_balance + amount_transferred)

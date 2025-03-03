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

import os
import argparse


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


#  get transaction arguments
parser = argparse.ArgumentParser()
parser.add_argument("--from", dest="from_account", required=True, type=str)
parser.add_argument("--to", dest="to_account", required=True, type=str)
parser.add_argument("--amount", required=True, type=float)
tran_args = parser.parse_args()

# transfers from to same account illegal
if tran_args.from_account == tran_args.to_account:
    exit("Own transfers not allowed")

# check for burglars
if tran_args.amount < 0:
    exit("Trying to steal money?")

# get ballance from both accounts
bank_path = "02/banka/"
sender_original_balance = get_acc_balance(os.path.join(bank_path, tran_args.from_account))
recipient_original_balance = get_acc_balance(os.path.join(bank_path, tran_args.to_account))

# check for sufficient account balance
if sender_original_balance - tran_args.amount < 0:
    exit(f"Transaction denied! No sufficient funds on account {tran_args.from_account}")

# set new account balance
set_new_acc_balance(os.path.join(bank_path, tran_args.from_account), sender_original_balance - tran_args.amount)
set_new_acc_balance(os.path.join(bank_path, tran_args.to_account), recipient_original_balance + tran_args.amount)

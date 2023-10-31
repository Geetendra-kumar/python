from brownie import Bank, accounts
import os


def main():
    bank = Bank.deploy({"from": accounts[0]})

    f = open(r"C:\Users\geete\Desktop\python\scripts\app\api\.env", "w")
    f.write("BANK_ADDRESS=" + str(bank))
    f.close()

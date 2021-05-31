#!/usr/bin/python3

from brownie import Token, accounts
import os

dev = os.getenv("PRIVATE_KEY")
dev = accounts.add(dev)

def main():
    return Token.deploy("Test Token One", "TST2", 18, 1e30, {'from': dev})

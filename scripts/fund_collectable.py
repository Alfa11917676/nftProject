from brownie import tokenCollectable
from scripts.help_scripts import fund_advanced_collectible

def main():
	token_collectable = tokenCollectable[len(tokenCollectable)-1]
	fund_advanced_collectible(tokenCollectable)
import pytest

from brownie import *
@pytest.fixture(scope="module")
def main(tokenHandlers, accounts):
	return tokenHandlers.deploy({'from': accounts[0]})


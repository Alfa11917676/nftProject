import pytest
def test_mapping(deploy, accounts):
	deploy.createTokens({'from':accounts[0]})
	assert deploy.tokenCounter == 1
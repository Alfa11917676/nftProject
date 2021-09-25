from brownie import accounts, tokenHandlers, tokenCollectable, config, network
import time

def main():
	dev = accounts.add(config['wallets']['from_key'])
	tokencollectable = tokenCollectable[len(tokenCollectable)-1]
	transaction = tokencollectable.createCollectible("None",{"from": dev})
	transaction.wait(1)
	time.sleep(10)
	requestId = transaction.events['requestedCollectible']['requestId']
	print(requestId)
	token_id = tokencollectable.requestIdToTokenId(requestId)
	print(f'The request id is {requestId}')
	print(f'The token id is {token_id}')

from brownie import accounts, tokenHandlers, tokenCollectable, config, network
from scripts.help_scripts import fund_advanced_collectible
def main():
	dev = accounts.add(config['wallets']['from_key'])
	print(network.show_active())
	publish_source = False
	tokencollectible = tokenCollectable.deploy(
		config['networks'][network.show_active()]['vrf_coordinator'],
		config['networks'][network.show_active()]['link_token'],
		config['networks'][network.show_active()]['keyhash'],
		{"from": dev},
		publish_source = publish_source
	)
	fund_advanced_collectible(tokencollectible)
	
	
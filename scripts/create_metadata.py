import json
import os
import requests
from brownie import accounts, tokenCollectable, network
from metaData import sample_metadata
from pathlib import Path

def main():
	print('Working on '+ network.show_active())
	token_collectable = tokenCollectable[len(tokenCollectable) - 1]
	number_of_tokens = token_collectable.tokenCounter()
	print(number_of_tokens)
	write_metadata(number_of_tokens, token_collectable)

def write_metadata(number_of_tokens, token_collectable):
	for token_id in range(number_of_tokens):
		collectable_metaData = sample_metadata.metadata_template
		metadata_file_name = ( 
			"./metaData/{}/".format(network.show_active()) + str(token_id)
		)
		if Path(metadata_file_name).exists():
			print(f'{metadata_file_name} already found')
		else:
			print(f'Creating {metadata_file_name}')
			collectable_metaData["name"]  = 'Arnab'
			collectable_metaData['description'] = f'{collectable_metaData["name"]} is great'
			# collectable_metaData['attributes'][0] = 'Fearless'
			attributes = collectable_metaData['attributes']
			attributes[0]['type'] = 'Fearless'
			attributes[0]['power'] = 'Sword'
			print(collectable_metaData)
			image_to_upload = None
			if os.getenv("UPLOAD_IPFS")=='true':
				image_path =  "./img/demo.png"
				image_to_upload = upload_to_ipfs(image_path)
			collectable_metaData['image'] = image_to_upload
			with open(metadata_file_name,'w') as file:
				json.dump(collectable_metaData, file)
			if os.getenv("UPLOAD_IPFS") == 'true':
				upload_to_ipfs(metadata_file_name)
def upload_to_ipfs(filepath):
	with Path(filepath).open('rb') as fp:
		image_binary = fp.read()
		ipfs_url = "http://localhost:5001"
		response = requests.post(ipfs_url+"/api/v0/add", files = {"file":image_binary})
		print(response.json())
		ipfs_hash = response.json()['Hash']
		fileName = filepath.split('/')[-1:][0]
		image_uri = "https://ipfs.io/ipfs/{}?filename={}".format(ipfs_hash, fileName)
		print(f'The filename is {fileName}, {ipfs_hash}, {image_uri}')
		
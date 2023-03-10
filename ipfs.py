import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	#with open("sample.json", "w+") as outfile:
	outfile =	json.dumps(data) 
	#print(outfile)
	files = {'file.json': str(outfile)}	
	#print(files)
	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=('2LgqjZLmpHnRS52JcP9fDQEH83S','205aa3dbd378a8f1bc392ddd6f9cbf15'))
	text = response.text
	json_object = json.loads(text)
	#print(text)
	#print('============')
	cid = json_object['Hash']
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	params = (('arg',cid),)
	response = requests.post('https://ipfs.infura.io:5001/api/v0/cat', params=params, auth=('2LgqjZLmpHnRS52JcP9fDQEH83S','205aa3dbd378a8f1bc392ddd6f9cbf15'))
	text = response.text
	#print(text)
	data = json.loads(text)
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data


#response = requests.post('https://web.archive.org/web/20221206091957/https://ipfs.infura.io:5001/api/v0/cat', files=files, auth=('2LgqjZLmpHnRS52JcP9fDQEH83S','205aa3dbd378a8f1bc392ddd6f9cbf15'))
#	print(response.text)
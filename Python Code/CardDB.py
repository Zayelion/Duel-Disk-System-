import json
import requests
import shutil

def Download_Img(Card_img_url,id_card):
	resp = requests.get(Card_img_url, stream=True)
	local_file = open('img/'+id_card+'.jpg', 'wb')
	resp.raw.decode_content = True
	shutil.copyfileobj(resp.raw, local_file)
	del resp



def Get_Card_Data(id_card):
	# Normalize IDs
	id_card = str(int(id_card))
	# Open Json DB
	with open('cardinfo.json', 'r') as json_file:
	    data = json.load(json_file)
	# Search for Card
	for card in data:
		if card["id"] == id_card:
			Card = {} 
			Card["url"] = card["card_images"][0]["image_url"]
			Card["id"] = card["id"]
			Card["name"] = card["name"]
			Card["atk"] = card["atk"]
			Card["def"] = card["def"]
			Card["lvl"] = card["level"]
			Card["des"] = card["desc"]
			Card["typ"] = card["type"]
			Card["atr"] = card["attribute"]
			Card["race"] = card["race"]
			
			# get image if not downloaded before
			try:
			    f = open('img/'+id_card+".jpg")
			    print("Card Image exists on local machine")
			    f.close()
			except IOError:
			    print("File not found, Downloading...")
			    Download_Img(Card["url"],id_card)
			    print("Done")

			return Card


# Card = Get_Card_Data(id_card = '59793705')
# print(Card)






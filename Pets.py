#! /opt/homebrew/bin/python3
# This is just a comment added to illustrate the use of version control.

Pets={'Dogs': [{'dog': 'Chia'}, {'dog': 'Pepe'}, {'dog': 'Dodo'}], 'Cats': [{'cat': 'Kiki'}, {'cat': 'Tigra'}, {'cat': 'Gris'}, {'cat': 'Clarito'}], 'Bunnies': [{'bunny': 'Luna'}, {'bunny': 'Rico'}, {'bunny': 'Coco'}]}

target_key = input("Enter type of pet:")
for key in Pets:
	if key == target_key:
		print(key,":")
		for pet_list in Pets[key]:
			for key2 in pet_list:
				print(pet_list[key2])
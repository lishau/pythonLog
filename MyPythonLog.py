>>> Pets ["Cats"] = []
>>> Pets
{'Dogs': [{'dog': 'Chia'}, {'dog': 'Pepe'}, {'dog': 'Dodo'}], 'Cats': []}
>>> Pets ["Cats"].append({"cat":"Kiki"})
>>> Pets
{'Dogs': [{'dog': 'Chia'}, {'dog': 'Pepe'}, {'dog': 'Dodo'}], 'Cats': [{'cat': 'Kiki'}]}
>>> Pets ["Cats"].extend([{"cat":"Tigra"}, {"cat":"Gris"},{"cat":"Clarito"}])
>>> Pets
{'Dogs': [{'dog': 'Chia'}, {'dog': 'Pepe'}, {'dog': 'Dodo'}], 'Cats': [{'cat': 'Kiki'}, {'cat': 'Tigra'}, {'cat': 'Gris'}, {'cat': 'Clarito'}]}
>>> print (keys in Pets)
Traceback (most recent call last):
  File "<python-input-95>", line 1, in <module>
    print (keys in Pets)
           ^^^^
NameError: name 'keys' is not defined
>>> For keys in Pets:
  File "<python-input-96>", line 1
    For keys in Pets:
    ^^^
SyntaxError: invalid syntax. Did you mean 'for'?
>>> for keys in Pets:
...     print(keys)
...
Dogs
Cats
>>> Pets ["Cats"] [1] ["cat"]
'Tigra'
>>> Pets ["Bunnies"] = [{"bunny":"Luna"}, {"bunny":"Rico"}]
>>> Pets
{'Dogs': [{'dog': 'Chia'}, {'dog': 'Pepe'}, {'dog': 'Dodo'}], 'Cats': [{'cat': 'Kiki'}, {'cat': 'Tigra'}, {'cat': 'Gris'}, {'cat': 'Clarito'}], 'Bunnies': [{'bunny': 'Luna'}, {'bunny': 'Rico'}]}
>>> Pets ["Bunnies"].append ({"bunny":"Coco"})
>>> Pets
{'Dogs': [{'dog': 'Chia'}, {'dog': 'Pepe'}, {'dog': 'Dodo'}], 'Cats': [{'cat': 'Kiki'}, {'cat': 'Tigra'}, {'cat': 'Gris'}, {'cat': 'Clarito'}], 'Bunnies': [{'bunny': 'Luna'}, {'bunny': 'Rico'}, {'bunny': 'Coco'}]}
>>> Pets ["Bunnies"] [2]
{'bunny': 'Coco'}
>>>

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))




    >> for key in Pets:
...         print (key, "the value is:", Pets[key])
...         for petdictionary in Pets[key]:
...                 for key in petdictionary:
...                         print (petdictionary[key])
...
Dogs the value is: [{'dog': 'Chia'}, {'dog': 'Pepe'}, {'dog': 'Dodo'}]
Chia
Pepe
Dodo
Cats the value is: [{'cat': 'Kiki'}, {'cat': 'Tigra'}, {'cat': 'Gris'}, {'cat': 'Clarito'}]
Kiki
Tigra
Gris
Clarito
Bunnies the value is: [{'bunny': 'Luna'}, {'bunny': 'Rico'}, {'bunny': 'Coco'}]
Luna
Rico
Coco
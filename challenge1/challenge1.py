#!/usr/bin/env python3
#Python Challenge Lab #1

dogs = ["mudge", "bingo"]
fish = ["dorothy", "nemo"]

pets = [{"type":"dog", "name": "mudge","age": 4}, 
	{"type":"dog", "name": "bingo","age": 12},
	{"type":"fish", "name": "nemo","age": 2},
	{"type":"fish", "name": "dorothy","age": "3 days"}]

for item in pets:	
    print(item)
    print(item["type"])
if item["type"] == "dog":
    dogs.append(item['name'])
    print(dogs)

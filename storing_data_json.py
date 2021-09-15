''' 

The json module allows you to dump simple python data structures into a file and 
load the data from a file the next time the program runs. 

You can also use json to share data between different Python programs. 

even better, the json data format is not specific to Python, 
so you can share to any other programmer. 

'''

# JSON ( Javascript Object Notation) format was before for Javascript, but most programs use it

# The first program is to store a set of numbers and another program that reads those numbers back to memory

# using json.dump() to store set numbers and json.load() to read.

# Example

import json


numbers = [2,3,5,7,11,13]

filename = 'numbers.json'

with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)



# now using json load...

with open(filename) as f_obj:
	numbers = json.load(f_obj)


# Saving and Reading user generated data 

username = input("What is your name?");

filename = 'username.json'
with open(filename, 'w') as f_obj:
	json.dump(username, f_obj)
	print("We will remember you when you comeback..")






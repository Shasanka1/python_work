
'''

Functions- 

	are blocks of code desgined to do one specific task that you've defined
'''

''' Example of function '''

def greet_user(username):
	""" Display a Message """
	x = 1
	while x<= 5:
		print("Hello " + username.title() + " !") 
		x+=1

greet_user('jesse')

	
""" 
Keyword arguments -

	is a name-value pair that you pass to a function. You directly associate the name and the value 

	with in the argument. 

"""

def desribe_pet(animal_t,pet_n):
	''' Display info of pet'''
	print("\nI have a " + animal_t + " . ")
	print("My " + animal_t + "'s name is " + pet_n.title() + " . ")

desribe_pet(animal_t = "hamster", pet_n = "harry")

""" The order of the keyword argument doesn't matter"""

desribe_pet(pet_n = "harry", animal_t = "hamster")



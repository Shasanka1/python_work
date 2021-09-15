"""

Testing Code
	- This proves that the code works as it is supposed to..


	1.) Lets Test a function

"""

# In order to test, you need code to test. Lets do a function that takes in first/last names..

def get_formatted_name(first,last):
	""" Generate a neatly formated full name """
	full_name = first + ' ' + last
	return full_name.title()

""" Check the testing part of this funciton in file testing_code.py """
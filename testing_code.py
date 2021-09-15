"""

This program is to test the testing_code_name_function.py function formatted name. 

"""

from testing_code_name_function import get_formatted_name

print(" Enter 'q' at any time to quit")
while True:
	first = input("\n Please give me your first name: ")
	if first == 'q':
		break
	last = input("\n Please give me your last name")
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)

	print("\tNeatly formated name : " + formatted_name + ".")






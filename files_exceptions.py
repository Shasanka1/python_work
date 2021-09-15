"""
	
	Now that you mastered soem basic skills in wrting organized programs. Now, time to make
	programs even more releavent and usable. Learn about files so programs can quickly analyze
	lots of data


"""

# Reading a file 

'''

  Reading a file is particularly useful in data analysis applications, but for any situation for 
  analyzing or modifying information stored in files. 

'''

# Lets read an entire file 

''' 

This program that will open a file, read it, and print the contents of the file on screen'''

with open('pi_digital.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

# Lets break this down

'''

 open - To do anything to a file, the first thing neede is open the file to access it. The function
 		needs one argument, the file name. Python looks it for in the directory. 


'''

# You can replace the text in open with path to the file. If the file is located in another folder/directory

# you can also have a file path anywhere in the system. Example..

file_path = '/Applications/Sublime Text 3/Backup/20180318214946/JavaScript Completions/node_binaries/osx-64bit/lib/node_modules/npm/node_modules/mkdirp/bin/usage.txt'

with open(file_path) as file_object:
	contents = file_object.read()
	print(contents.rstrip())


# Reading Line by Line

filename = 'pi_digital.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line)


# Editing the read out of files:

with open(filename) as file_object:
	lines = file_object.readlines()


pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))


'''


# Writing to an empty file

'''

filename = 'programmers.txt'

# with open(filename, 'w') as file_object:
# 	file_object.write("I love Programming!")



'''

The second argument in open(first,second) tells Python which mode we are in.
'w' - write mode
'r' - read mode -- The Default setting
'a' - append mode
'r+' - which allows to read & write on file



'''

# Note, Python can only write Strings to a text file. If you want store numbers in text
# you'll need to convert data to string format first using str() function

with open(filename, 'w') as file_object:
	file_object.write("I love Programming!")
	file_object.write("\nI love creating new games")
	file_object.write("\n" + str(22/7))


# a - Example of appending to a file - Means to add on content to file instead of writing over

with open(filename, 'a') as file_object:
	file_object.write("\n I also love finding meaning in large datasets!\n")
	file_object.write("I love creating apps that can run in browser")


# Guest Name

# name = ""

# while name != 'Q':
# 	name = input("Please Enter your name : ")
# 	with open('guest.txt', 'a') as file_object:
# 		file_object.write(name)


'''

  Exeptions
  	- Whenever an error occurs that makes Python unsure what to do next, it creates an exception object

  	- If yoy write code to handle exception, the program will continue. If you don't, the program halt and show
  	a tracebook , which includes a report of the exception that was raised. 

  	- Exceptions are handled with a try-except block. this means that the program will still work if things 
  	start to go wrong. It also tells Python what to do if exception is raised. 


'''


# Handling ZeroDivisionError Exception

#print(5/0); #This causes a division by zero error


# Python Created a ZeroDivisionError Exception object in response to situation. Now we can modify this..

try:
	print(5/0)
except ZeroDivisionError:
	print("You Can't divide by Zero!")


# Exceptions can also be used to prevent crashes. Example.. User input. If wrong answer, not crash
# but helping user out with valid input can help

# print("Give me two numbers , and I'll divide them . ")
# print("Enter 'q' to quit.")

# while True:
# 	first_number = input ("\n First number: ")
# 	if first_number == 'q':
# 		break;
# 	second_number = input("\n Second Number: ")
# 	if second_number == 'q':
# 		break;
# 	answer = int(first_number)/int(second_number)
# 	print(answer)



# The use of else block in the try-except to be more effective in the code
# while True:
# 	first_number = input ("\n First number: ")
# 	if first_number == 'q':
# 		break;
# 	second_number = input("\n Second Number: ")
# 	try:
# 		answer = int(first_number)/int(second_number)
# 	except ZeroDivisionError:
# 		print("You can't divide by 0!!!")
# 	else:
# 		print(answer)


# Every success of the Try block is moved to the else block to continue the program

''' 

Handeling the FileNotFoundError Exception 

    - One common issue is working with files is handling missing files. Either mispealed,
     might be in different location, or file not exist. You can handle all those situations 


 Example - 
 	   Lets try read a file that doesn't exist. 



'''

# filename = 'alice.txt'

# with open(filename, encoding = 'utf-8') as f_obj:
# 		contents = f_obj.read()



''' Dealing with this error '''

filename = 'alice.txt'

try:
	with open(filename, encoding = 'utf-8') as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist"
	print(msg)


'''
One cool thing about strings is that they can be split into a list of words from a string.

This is used by the method split()

'''
# title = " Alice in Wonderland"
# print(title.split())


# You can use this slit method even for exception handling. Adding on to the FileNotFoundError

# try:
# 	with open(filename, encoding = 'utf-8') as f_obj:
# 		contents = f_obj.read()
# except FileNotFoundError:
# 	msg = "Sorry, the file " + filename + " does not exist"
# 	print(msg)
# else:
# 	# Count the approximate number of words in the file.
# 	words = contents.split()
# 	num_words = len(words)
# 	print("The File " + filename + " has about " + str(num_words) + " words")


# To make this general to all files for counting the words in the file, lets turn it to a functions


def count_words(filename):
	try:
		with open(filename, encoding = 'utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
			msg = "Sorry, the file " + filename + " does not exist"
			print(msg)
	else:
			# Count the approximate number of words in the file.
			words = contents.split()
			num_words = len(words)
			print("The file " + filename + " has about " + str(num_words) + " words")

filename = 'alice.txt'
count_words(filename)







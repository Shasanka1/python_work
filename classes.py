"""

Classes- 

Object orieted programming is one of the most effective approaches to writing software. In object
- oriented programming write classes that represent real-world things
and situations, and you create objects based on thosese classes. 

Making an object from a class is called 'instantiation ' you wil work with instance of classes


"""

# Creating and using a class

# Creating a dog class

class Dog(): # the empty paramthesis are because creating this class from scratch
	"""string for """
	def __init__(self, name, age):
		""" Initalize name and age attributes"""
		self.name = name
		self.age = age

	def sit(self):
		""" Simulate a dog sitting in response to command"""
		print(self.name.title() + " is now sitting. ")

	def roll_over(self):
		print(self.name.title() + " roll over !")


"""
            The _init_()  Method is a spcial method Python runs automatically whenever
            we create an instance of the  Dog class. 

            "self " - represent an instance of the class. It allows attributes and 
            methods of the class to be accessed. Example below....

			
			Any variable prefixed with self is available to every method in the class, and we'll also be
			able to access these variables through an instance created from the class. Example below....

     

"""

# Making an instance of a class. Example Dog.

my_dog = Dog('willie', 6)
print("My Dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old \n") 

# calling the methods

my_dog.sit()
my_dog.roll_over()



'''

Inheritence in Python Programming Classes. Example cars


'''
class Car():
	"""docstring for Car"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_description_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()


class ElectricCar(Car):
	"""docstring for ElectricCar"""
	def __init__(self, make, model, year):
		super(ElectricCar,self).__init__( make, model, year)


# Example of running inheritence

my_tesla = ElectricCar('tesla', 'model s', 2016)
print("\n"+my_tesla.get_description_name())
		


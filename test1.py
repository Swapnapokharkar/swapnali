
#Write a Program to Swap two Variables.
# Created a Class
class Program:
	# Created Parameterized Constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s
	# Funcion to Swap Variables
	def calculate(self):
		self.first , self.second= self.second , self.first

	#Function to Display Variables
	def display(self):
		print("Swapped Variable F: " + str(self.first))
		print("Swapped Variable S: " + str(self.second))
obj = Program(input("Enter Variable F: "),input("Enter Variable S: "))

# Perform Swap
obj.calculate()

# display result
obj.display()



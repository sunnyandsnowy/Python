
class User():
	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName
		self.loginAttempts = 0
	
	def describeUser(self):
		self.fullName = self.firstName +" " + self.lastName
		print("The full name: " + self.fullName)
		
	def greetUser(self):
		print("Hello! " + self.firstName + " " + self.lastName)
		
	def incrementLoginAttempts(self):
		self.loginAttempts += 1
		
	def resetLoginAttempts(self):
		self.loginAttempts = 0

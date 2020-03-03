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

class Admin(User):
	#def __init__(self,firstName, lastName,privileges=[]):
	def __init__(self,firstName, lastName):
		super().__init__(firstName,lastName)
		#self.privileges = privileges
		self.privileges = Privileges()
	
	#def showPrivileges(self):
	#	print("Privileges: ")
	#	for privilege in self.privileges:
	#		print(privilege)
	
	
class Privileges():
	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']
		
	def showPrivileges(self):
		print("Privileges: ")
		for privilege in self.privileges:
			print(privilege)
			

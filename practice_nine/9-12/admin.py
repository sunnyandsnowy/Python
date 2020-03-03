from user import User

class Admin(User):
	#def __init__(self,firstName, lastName,privileges=[]):
	def __init__(self,firstName, lastName):
		super().__init__(firstName,lastName)
		#self.privileges = privileges
		self.privileges = Privileges()

class Privileges():
	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']
		
	def showPrivileges(self):
		print("Privileges: ")
		for privilege in self.privileges:
			print(privilege)

from collections import OrderedDict
from random import randint
class Restaurant():
	def __init__(self,restaurantName,cusineType):
		self.restaurantName = restaurantName
		self.cusineType = cusineType
		self.numberServed = 0
		
	def describeRestaurant(self):
		print("The restaurant's name: "+self.restaurantName.title())
		print("The cusine's type: "+self.cusineType.title())
	
	def openRestaurant(self):
		print("The restaurant is opening!")
		
	def setNumberServed(self, numberServed):
		self.numberServed = numberServed
		
	def incrementNumberServed(self, number):
		self.numberServed += number
	
#restaurant = Restaurant('red','lucai')
#print(restaurant.restaurantName)
#print(restaurant.cusineType)
#restaurant.describeRestaurant()
#restaurant.openRestaurant()


#restaurantOne = Restaurant('white','yuecai')
#restaurantTwo = Restaurant('green','beijingcai')
#restaurantThree = Restaurant('blue','yunnancai')

#restaurantOne.describeRestaurant()
#restaurantTwo.describeRestaurant()
#restaurantThree.describeRestaurant()

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

#userOne = User('zm', 'li')
#userTwo = User('yu', 'yang')

#userOne.describeUser()
#userOne.greetUser()

#userTwo.describeUser()
#userTwo.greetUser()


#restaurant = Restaurant('red','diancai')
#print("numberServed: " + str(restaurant.numberServed))
#restaurant.numberServed = 5
#print("numberServed: " + str(restaurant.numberServed))
#restaurant.setNumberServed(63)
#print("numberServed: " + str(restaurant.numberServed))
#restaurant.incrementNumberServed(5)
#print("numberServed: " + str(restaurant.numberServed))

#user = User('jack', 'james')
#print("loginAttempts: " + str(user.loginAttempts))
#user.incrementLoginAttempts()
#user.incrementLoginAttempts()
#print("loginAttempts: " + str(user.loginAttempts))
#user.resetLoginAttempts()
#print("loginAttempts: " + str(user.loginAttempts))

class IceCreamStand(Restaurant):
	def __init__(self,restaurantName,cusineType,flavors=[]):
		super().__init__(restaurantName,cusineType)
		self.flavors = flavors
	
	def showFlavors(self):
		print("Icecream flavors: ")
		for falvor in self.flavors:
			print(falvor)

#iceCream = IceCreamStand('red','chuancai',['white','brown'])
#iceCream.flavors.append('red')
#iceCream.flavors.append('yellow')
#iceCream.flavors.append('blue')
#iceCream.showFlavors()

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
			
#admin = Admin('zm','z',['can add post', 'can delete post',])
#admin.privileges.append('can ban user')
#admin.showPrivileges()

class Privileges():
	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']
		
	def showPrivileges(self):
		print("Privileges: ")
		for privilege in self.privileges:
			print(privilege)
			
#admin = Admin('zm', 'z')
#admin.privileges.showPrivileges()

class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometerReading = 0
		
	def getDescriptiveName(self):
		longName = str(self.year) + ' ' + self.make + ' ' + self.model
		return longName.title()
		
	def readOdometer(self):
		print('This car has ' + str(self.odometerReading) + ' miles on it.')
	
	def updateOdometer(self,mileage):
		if mileage >= self.odometerReading:
			self.odometerReading = mileage
		else:
			print("You can't roll back an odometer!")
		
	def incrementOdometer(self,miles):
		self.odometerReading += miles
	
class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()
		
class Battery():
	def __init__(self, batterySize=70):
		self.batterySize = batterySize
		
	def describeBattery(self):
		print("This car has a " + str(self.batterySize) + "-kwh battery.")
	def getRange(self):
		if self.batterySize == 70:
			range = 240
		elif self.batterySize == 85:
			range = 270
			
		message = 'This car can go approximately ' + str(range)
		message += ' miles on a full charge.'
		print(message)
	
	def upgradeBattery(self):
		if self.batterySize != 85:
			self.batterySize = 85
			
#myTesla = ElectricCar('tesla', 'model s', 2016)
#myTesla.battery.getRange()
#myTesla.battery.upgradeBattery()
#myTesla.battery.getRange() 

#languages = OrderedDict()

#languages['print'] = 'show something'
#languages['input'] = 'get something form users'
#languages['for'] = 'recycle'
#languages['if-elif-else'] = 'judge'
#languages['break'] = 'stop recycle'
#for language, using in languages.items():
#	print(language.title() + ": " + using.title())

class Die():
	def __init__(self):
		self.sides = 6
		self.range = 6
		self.rollNumber = 10
	
	def rollDie(self):
		self.sides = randint(1,self.range)
		print("骰子的的点数为:" + str(self.sides))
	
	def setRange(self,range):
		if range >=1:
			self.range = range
		else:
			print("The range is fault")
	
	def serRollNumber(self,rollNumber):
		self.rollNumber = rollNumber
	
	def showSides(self):
		currentNumber = 0
		while currentNumber < self.rollNumber:
			self.rollDie()
			currentNumber += 1
			if currentNumber == self.rollNumber:
				print()
	
die = Die()
die.showSides()
die.setRange(10)
die.showSides()
die.setRange(20)
die.showSides()

#要了解Python标准库 资源网站为：Python Module of the Week
#网址：http://pymotw.com/

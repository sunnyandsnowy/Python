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

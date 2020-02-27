#coding=gbk
#car = input("What kind of cars would you like? ")
#print("Let me see if I can find you a "+car.title())

#peopleNumber = input("How many people do we have? ")
#peopleNumber = int (peopleNumber)
#if peopleNumber >8:
#	print("We don't have enough tables")
#else:
#	print("We just have one table")

#number = input("Please input a number: ")
#number = int(number)
#if number % 10 == 0:
#	print(str(number)+" is a multiple of ten")
#else:
#	print(str(number)+" is not a multiple of ten")	

#prompt = "Please input what toppings do you want to add: "
#prompt += "\nEnter quit to end the adding  "
#toppings =""
#while toppings != 'quit':
#	toppings = input(prompt)
#	if toppings != 'quit':
#		print("We will add " + toppings.title()+"\n")
	
#prompt = "Please input your age"
#prompt += "\nEnter quit to end the program  "
#age = ""
#active = True
#while age != 'quit' or active == True:
#	age = input (prompt)
#	if age == 'quit':
#		active = False
#		break
#	age = int(age)
#	if age<3:
#		print("free\n")
#	elif age>= 3 and age <=12:
#		print("ten dollars\n")
#	else:
#		print("fifteen dollars\n")
	
#while True:
#	print("1")

#sandwichOrders = ['red', 'blue', 'yellow']
#finishedsandwiches = []
#while sandwichOrders:
#	sandwichOrder = sandwichOrders.pop()
#	print("I made your "+ sandwichOrder + " sandwich")
#	finishedsandwiches.append(sandwichOrder)
#print("Here are all sandwiches: ")
#for sandwichOrder in finishedsandwiches:
#	print(sandwichOrder)

#sandwichOrders = ['red','pastrami', 'blue','pastrami' ,'yellow','pastrami']
#print("We ran out of pastrami")
#while 'pastrami' in sandwichOrders:
#	sandwichOrders.remove('pastrami')
#finishedsandwiches = []
#while sandwichOrders:
#	sandwichOrder = sandwichOrders.pop()
#	print("I made your "+ sandwichOrder + " sandwich")
#	finishedsandwiches.append(sandwichOrder)
#print("Here are all sandwiches: ")
#for sandwichOrder in finishedsandwiches:
#	print(sandwichOrder)

dreamPlaces = {}
active = True
while active:
	name = input("What's your name: ")
	dreamPlace = input("If you could visit one place in the world, where would you go: ")
	dreamPlaces[name]=dreamPlace
	repeat = input("Would you like to let another person respond?(yes/no): ")
	if repeat.lower() == 'n':
		active = False
print(dreamPlaces)

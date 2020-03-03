import json #导入模块json

#文件读写操作
#with open('learningPython.txt') as fileWork:
	 #contents = fileWork.read() #方法一
	 #print(contents)
	#for line in fileWork: #方法二
	#	print(line.rstrip())
#	lines = fileWork.readlines()
#for line in lines:
#	print(line.rstrip())

#with open('learningPython.txt') as fileObject:
#	for line in fileObject:
#		line = line.replace("Python",'C')
#		print(line)

#fileName = 'guest.txt'
#with open(fileName,'w') as fileObject:
#	usersName = input("Please input you name: ")
#	fileObject.write(usersName)

#fileName = 'guestBook.txt'
#with open(fileName,'w') as fileObject:
#	while True:
#		print("Please input your name. "+
#			"\nEnter 'q' to end the program")
#		usersName = input("Name: ")
#		if usersName.lower() == 'q':
#			break
#		print("Hello! "+ usersName.title()+"\n")
#		fileObject.write(usersName+"\n")

#fileName = 'reasons.txt'
#with open(fileName,'a') as fileObject:
#	while True:
#		print("Why are you like making program"+
#			"\nEnter 'q' to end the program")
#		reason = input("Reason: ")
#		if reason.lower() == 'q':
#			break
#		print()
#		fileObject.write(reason+"\n")
		


#异常操作
#加法运算

#print("Please input two numbers: ")
#print("Enter 'q' to end the programing.")
#while True:     #改进为加法器
#	try :
#		firstNumber = input("First number: ")
#		if firstNumber == 'q':
#			break
#		firstNumber = int(firstNumber)
#		secondNumber = input("Second number: ")
#		if secondNumber == 'q':
#			break
#		secondNumber = int(secondNumber)
#		print(firstNumber + secondNumber)
#		print()
#	except ValueError:
#		print("请不要输入字符串\n")

#文件异常操作
#def showFile(fileName):
#	try:
#		with open(fileName) as fileObject:
#			contents = fileObject.read()
#	except FileNotFoundError:
		#print("The " + fileName + " does not exist.")
#		pass   #让程序一言不发
#	else:
#		print(contents)
		
#fileNames = ['cats.txt', 'dogs.txt']

#for fileName in fileNames:
#	showFile(fileName)

#常见单词（统计某本书中的单词数）
#访问项目Gutenberg(http://gutenberg.org/),可找到一些你想分析的图书
#fileName = "傲慢与偏见.txt"

#try:
#	with open(fileName,'r', encoding = 'utf-8') as fileObject:
		#UnicodeDecodeError: 'gbk' codec can't decode byte 0xbf 
		#in position 2: illegal multibyte sequence 解决方法，显示表示encoding
		
#		contents = fileObject.read()
#except FileNotFoundError:
#	print(fileName + "不存在。")
#else:
#	counts = contents.lower().count('the')
#	print(counts)

#存储数据
#numbers = [2, 3, 5, 7, 11, 13]

fileName = 'numbers.json'
#with open(fileName,'w') as fileObject:
   #存入数据
#	json.dump(numbers,fileObject)

#with open(fileName) as fileObject:
	#读取数据
#	numbers = json.load(fileObject)

#print(numbers)

# 喜欢的数字（可储存和读取数字）
#fileName = 'favorite_numbers.json'

#with open(fileName,'w') as fileObject:
	#存储
#	number = input('Plese input you favorite number: ')
#	json.dump(number,fileObject)

#with open(fileName) as fileObject:
	#读取
#	number = json.load(fileObject)
#	print(number)

#记住喜欢的数字
#fileName = 'favorite_number.json'

#def getStoreNumber():
#	"""获取存储的信息"""
#	try:
#		with open(fileName) as fileObject:
#			number = json.load(fileObject)
#	except FileNotFoundError:
#		return None
#	else:
#		return number

#def getFavoriteNumber():
#	"""获取用户最喜欢的数字"""
#	number = input('Please input you favorite number: ')
#	with open(fileName,'w') as fileObject:
#		json.dump(number,fileObject)
#	return number
	
#def favoriteNumber():
#	number = getStoreNumber()
#	if number == None:
#		number = getFavoriteNumber()
#		print("I will rember your favorite number!"）
#	else:
#		print("Your favorite number is: " + number)	
		
#favoriteNumber()

#验证用户
#def getStoreUserName():
#	"""如果存储了用户名就获取它"""
#	fileName = 'user_name.json'
#	try:
#		with open(fileName) as fileObject:
#			userName = json.load(fileObject)
#	except FileNotFoundError:
#		return None
#	else:
#		return userName


#def getNewUserName():
#	"""提示用户输入用户名"""
#	userName = input("What is your name? ")
#	fileName = 'user_name.json'
#	with open(fileName,'w') as fileObject:
#		json.dump(userName,fileObject)
#	return userName
	
#def greetUser():
#	"""问候用户，并指出其名字"""
#	userName = getStoreUserName()
	
#	if userName:
#		print(userName + " is you name?")
#		answer = input('please enter y or n: ')
#		if answer.lower() == 'y':
#			print('Welcome back, ' + userName + '!')
#		else:
#			userName = getNewUserName()
#			print('We will rember you when you come back, ' + userName + "!")
#	else:
#		userName = getNewUserName()
#		print('We will rember you when you come back, ' + userName + "!")
		
#greetUser()

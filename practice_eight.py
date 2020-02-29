#coding=gbk
#import printingFunctions#导入整个模块
#from printingFunctions import printModels,showCompletedModels#导入特定函数
#from printingFunctions import printModels as pm ,showCompletedModels as scm#给函数指定别名
#import printingFunctions as pf #给模块指定别名
#from printingFunctions import* #通过名称调用每个函数
#def displayMessage():
#	"""打印信息"""
#	print("I will learn function.")
#displayMessage()

#def favoriteBook(title):
#	"""打印消息"""
#	print("One of my favorite books is "+ title.title())
#favoriteBook("alice in wonderland")

#def makeShirt(size,words):
#	print("The T-shirt's size: " + size)
#	print("The T-shirt's words: " +words)
#makeShirt("s",'zzm')
#makeShirt( words = "zzmshuai",size = "XXX")
#def makeShirt(size = 'L',words = 'I love Python'):
#	print("The T-shirt's size: " + size)
#	print("The T-shirt's words: " +words)
#	print()
#makeShirt()
#makeShirt('M')
#makeShirt(words = 'I love study')

#def describeCity(city,nation = 'China'):
#	print(city.title() + " is in " + nation.title())
#describeCity('wuhang')
#describeCity("kunming")
#describeCity("moscow",'russia')

#def cityCountry(cityName,nation):
#	print(cityName.title()+", "+nation.title())
	
#cityCountry('santiago','chile')
#cityCountry('beijing','china')
#cityCountry('newyork','america')

#def makeAlbum(singerName,albumName,number=''):
#	album={'singerNmae': singerName,'albumName':albumName}
#	if number:
#		album['number'] = number
#	return album
#album1=makeAlbum('zzm','ab','1')
#album2=makeAlbum('ssa','ak')
#album3=makeAlbum('su','gh','2')
#print(album1)
#print(album2)
#print(album3)

#def makeAlbum(singerName,albumName,number=''):
#	album={'singerNmae': singerName,'albumName':albumName}
#	if number:
#		album['number'] = number
#	return album
	
#while True:
#	print("Please input singerName and albumName: ")
#	print("Enter 'q' to end the program")
#	singerName = input("Input singerName: ")
#	if singerName =='q':
#		break
#	albumName = input("Input albumName: ")
#	if albumName=='q':
#		break
#	album = makeAlbum(singerName,albumName)
#	print()
#	print(album)
#	print()


#def showMagicians(magicians):
#	for magician in magicians:
#		print(magician)
		
#def makeGreat(magicians):
#	number = 0
#	for magician in magicians:
#		magicians[number]='the Great '+magician
#		number +=1
#	return magicians
		
#magicians = ['zzm','ab','cd']
#magicians_1 = makeGreat(magicians[:])
#showMagicians(magicians)
#showMagicians(magicians_1)

#def sandwiches (*toppings):
#	print("toppings:")
#	for topping in toppings:
#		print(topping)
#	print()
#sandwiches("red")
#sandwiches('blue','green')
#sandwiches("grey",'yellow','purple')

#def buildProfile(first,last,**userInfo):
#	profile={}
#	profile['first']=first
#	profile['last']=last
#	for key, value in userInfo.items():
#		profile[key]=value
#	return profile
#userProfile = buildProfile('z','zm',age = 20,location = 'kunming',filed = 'art')
#print(userProfile)

#def carInformations(manufacture,model,**anyelses):
#	carInformation={}
#	carInformation['manufacture'] = manufacture
#	carInformation['model'] = model
#	for key, value in anyelses.items():
#		carInformation[key] = value
#	return carInformation
#car = carInformations('subaru', 'outback', color = "blue", tow_package = 'True')
#print(car)

#将函数储存在模块中
unprintedDesigns = ['iphone case', 'robot pendant', 'dodecahedron']
completedModels = []
printModels(unprintedDesigns,completedModels)
showCompletedModels(completedModels)

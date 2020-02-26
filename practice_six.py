#coding=gbk
#person = {'firstName':'jack','lastName':'james','age':18,'city':'kunming'}
#print(person['firstName'])
#print(person['lastName'])
#print(person['age'])
#print(person['city'])

#favoriteNumbers = {'zzm':0,'hyc':1,'lt':2,'xzx':3,'jack':5}
#print("zzm's favorite number is "+ str(favoriteNumbers['zzm'])+
#	".")
#print("hyc's favorite number is "+ str(favoriteNumbers['hyc'])+
#	".")
#print("lt's favorite number is "+ str(favoriteNumbers['lt'])+
#	".")
#print("xzx's favorite number is "+ str(favoriteNumbers['xzx'])+
#	".")
#print("jack's favorite number is "+ str(favoriteNumbers['jack'])+
#	".")

#dictionary = {'cin' :'C++中用于输入','cout' :'C++中用于输出', 'printf':"C语言中输出",'scanf' :'C语言中输入','lower': 'Python中将所以字母转换成小写字母'}
#print("cin: "+dictionary['cin']+".")
#print("cout: "+dictionary['cout']+".")
#print("printf: "+dictionary['printf']+".")
#print("scanf: "+dictionary['scanf']+".")
#print("lower: "+dictionary['lower']+".")

#dictionary = {'cin' :'C++中用于输入','cout' :'C++中用于输出', 'printf':"C语言中输出",'scanf' :'C语言中输入','lower': 'Python中将所以字母转换成小写字母',
#				'\n':"换行符",
#}
#for key,value in dictionary.items() :
#	print(key+" : "+value)

#rivers = {
#	'yangtze':"China",
#	'yellow':"Chian",
#	'nile':"egypt",
#	}
#for key, value in rivers.items():
#	print("The "+key.title()+" runs through "+value.title())

#for key in rivers.keys():
#	print(key.title())

#for value in rivers.values():
#	print(value.title())

#favoriteLanguages = {
#	'jen':'python',
#	'sarah':'c',
#	'edward':'ruby',
#	'phil':'python',
#}
#persons = ['jen','jack','ann','phil','john']
#for person in persons:
#	if person in favoriteLanguages.keys():
#		print("Thank you")
#	else:
#		print("Please take part in our survery")

#person1 = {'firstName':'jack','lastName':'james','age':18,'city':'kunming'}
#person2 = {'firstName':'ann','lastName':'carry','age':18,'city':'bejing'}
#person3 = {'firstName':'luce','lastName':'ken','age':18,'city':'shanghai'}
#persons = [person1,person2,person3]
#for person in persons:
#	name = person['firstName']+" "+ person['lastName']
#	age = person['age']
#	city = person['city']
#	print("\nname: " + name+"\nage: " + str(age)+"\ncity: "+city)
	
#mi = {'kind': 'dog', 'owner':'jack'}
#xi = {'kind': 'cat', 'owner':'mike'}
#la = {'kind': 'rabbit', 'owner':'ann'}
#pets = [mi, xi, la]
#for pet in pets:
#	print("kidn: "+pet['kind']+"  owner: "+pet['owner'])

#favoritePlaces = {'jack':['beijing','shanghai'],'mike':['shenzhen','xian','dunhuang'],'herry':['kunming','chengdu','chongqing']}
#for key,values in favoritePlaces.items():
#	print("\n"+key+' like to go:')
#	for value in values:
#		print(value)
		 
#favoriteNumbers = {'zzm':[0,23,1],'hyc':[1,49,5],'lt':[2,5,68],'xzx':[3,65,78],'jack':[5,85,7]}
#for name,numbers in favoriteNumbers.items():
#	print(name+"likes numbers is:")
#	for number in numbers:
#		print(str(number))
#	print("\n") 

cities = {'kunming':{'nation':'china','population':'100万','fact':'beautiful'},
	'newYork':{'nation':'america','population':'1500万','fact':'cold'},
	'singapore':{'nation':'singapore','population':'500万','fact':'hot'},
	}
for city, informations in cities.items():
	print(city+":")
	print('nation: ' + informations['nation'])
	print('population: ' + informations['population'])
	print('fact: ' + informations['fact'])
	print("\n")

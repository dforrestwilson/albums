#matches top owners of a given stock ticker using data from a downloaded bloomberg file of ownership. 
#Helps to determine which institutions have strong cross-ownership of stocks within a given sector/industry

def matcher():
	import csv
	match = []
	nomatch = []
	f = open(filepath)
	comp1 = f.read()
	complist = comp1.split(',,,,,,\n') #parsing bad file notation
	f = open(otherfilepath) #opening the comp file
	comp2 = f.read()
	comp2list = comp2.split(',,,,,,\n')
	for x in complist:
		if x in comp2list:
			match.append(x)
		else:
			nomatch.append(x)
	return match, no match
	

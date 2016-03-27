import sys, os
import pandas as pd

#takes input formatted excel files and creates a list of the overlapping locations for each company, including competitors
path = filepath specified by user
listoffiles = listiterating(path)
complete = buildlist(listoffiles)
fullist = search(complete)

def listiterating(filename):
	#taking a directory path as an input, builds a list of files within a folder
	onlyfiles = [f for f in os.listdir(path)]
	print 'Total Files'
	print len(onlyfiles)
	return onlyfiles

def runlist(filename):
	os.chdir('redirect to new folder path if needed')
	#opens file, imports, and outputs a dictionary of each files records
	raw = pd.read_excel(filename, skiprows=[0,1,2,3], parse_cols=[0,2,3,4,5])
	df = pd.DataFrame(raw)
	#probably an easier way but this works for now to get from excel to dictionary 
	converted = df.to_dict('records')
	return converted

def buildlist(listoffiles):
	#placing a bunch of list of dictionaries together in one list
	complete = []
	for x in listoffiles:
		print 'execting for %s' % x
		complete.append(runlist(x))
	return complete

def search(complete):
	#searching through the full list for footprints which overlap by city, county, state, etc
	trial = []
	for y in complete:
		for x in complete:
			for subdicts in y:
				for otherdicts in x:
					if otherdicts['Parent Company'] != subdicts['Parent Company'] and (otherdicts['City or Community'], otherdicts['State']) == (subdicts['City or Community'], subdicts['State']):
						#constructing a merged dictionary entry for each pair of matching locations and then appending to a list
						package = {'City':otherdicts['City or Community'],
						'County':otherdicts['County'],
						'State':otherdicts['State'],
						'Company':subdicts['Parent Company'],
						'Date Operational':subdicts['Date Operational'],
						'Competition':otherdicts['Parent Company'],
						'Comp Date Operational':otherdicts['Date Operational']}
						trial.append(package)
	return trial

def outputcsv(fullist):
	#outputs resulting list of dictionaries to a csv
	fieldnames = sorted(list(set(k for d in fullist for k in d)))
	with open(outputcsvfile, 'wb') as csvfile:
		writer = csv.DictWriter(csvfile, fieldname=fieldname, dialect='excel')
		#writing the header columns
		writer.writeheader()
		for x in fullist:
			#writing each dictionary as an Excel row
			writer.writerow(x)

	
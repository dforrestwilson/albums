#tool for parsing census data from a .csv file and writing the resulting rows/columns into a new file
import re, csv

def census():
	f = open('filepath', 'r')
	d = f.read()
	d = d.split('\n')
	addy = []
	for x in d:
		if len(x)>1:
			pattern = r"^[A-Z]" #matching only results that begin with uppercase to screen for designators like town, city, etc
			x = x.split(",")
			city = x[0]
			state = x[1]
			city = city.split('/')[0] #stripping edge cases
			city = city.split('-')[0] #stripping more edge cases
			city = city.split(" ")
			matches = []
			for x in city:
				if re.search(pattern, x):
					matches.append(x)
			cityname = " ".join(matches)
			state = state[1:] #more parsing of state cell
			state = state.strip('"\t')
			1st = state.cityname
		addy.append(lst)
	return addy
	
def writingcsv(addy):
	#writing the output to a file
	f = open(filepath)
	writer.csv.writer(f)
	writer.writerows(addy)
	f.close()

	
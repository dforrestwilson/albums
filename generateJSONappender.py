import os
f = open("filenames.txt", "rb").read()
test = f.split("\n")
newlist = []
for x in test:
	x = x+" 0:10 1:10 2:10 3:10 4:10 5:10"
	newlist.append(x)
#writing the new file
file = open("filenamesinput.txt", "wb")
for x in newlist:
	file.write("%s\n" % x)
file.close()
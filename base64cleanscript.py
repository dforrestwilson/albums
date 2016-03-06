#takes a folder of provided .jpg images and creates base64 copies, placing them in a specified folder
def base64creator("foldernamewithimages"):
	import os, base64
	from os import walk
	from os import listdir
	from os.path import isfile, join
	os.chdir("foldernamewithimages")
	imgs = [name for name in os.listdir() if name.endswith(".jpg")]
	#creating a single list of all files in the folder ending with .jpg
	for image in imgs:
		#creating a .txt named for the new file
		image64name = image.replace(".jpg",".txt")
		#encoding the image as base64
		image_64 = base64.encodestring(open(image,"rb").read())
		#switching to a specified folder to to write new files in
		os.chdir("newfolderwithbase64cleanedfiles")
		#writing the new file
		file = open(image64name, "wb")
		file.write(image_64)
		file.close()
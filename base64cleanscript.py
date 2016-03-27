#takes a folder of provided .jpg images and creates base64 copies, placing them in a specified folder
def base64creator():
	import os, base64
	from os import walk
	from os import listdir
	from os.path import isfile, join
	os.chdir("C:/Users/Noble/Pictures/AlbumArt")
	imgs = []
	for name in os.listdir("C:/Users/Noble/Pictures/AlbumArt"):
		if name.endswith(".jpg") or name.endswith(".png") or name.endswith(".itc2"):
			imgs.append(name)
	#creating a single list of all files in the folder ending with .jpg
	for image in imgs:
		os.chdir("C:/Users/Noble/Pictures/AlbumArt")
		#creating a .txt named for the new file
		#removing all the nasty special characters and spaces
		image64name = image.split('.')[0]
		image64name = ''.join(e for e in image64name if e.isalnum())
		image64name = image64name + ".txt"
		#encoding the image as base64
		try:
			image_64 = open(image,"rb").read()
			image_64 = base64.b64encode(image_64)
			#switching to a specified folder to to write new files in
			os.chdir("C:/Users/Noble/Desktop/test1/cleanbase64")
			#writing the new file
			f = open(image64name, "wb")
			f.write(image_64)
			f.close()
		except:
			print 'Error'
			pass
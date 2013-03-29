import os


file_list = os.listdir("/home/ahmed")
for items in file_list:
	if items[-3:] == ".py":
		print items




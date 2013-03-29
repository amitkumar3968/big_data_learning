import string

  

file = open("words.txt",  "rb")
for line in file:
    word =  line.strip()
    print word


file.close()

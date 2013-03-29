try:
    file_open = open("output1.txt",  'w')
    line = "This is the line we will write to file now !!"
    file_open.write(line)
    file_open.close()
except:
    print "Something went wrong !! "

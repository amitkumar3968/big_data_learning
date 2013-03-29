import string
import matplotlib.pyplot as plt
import collections 
import random

fh = open("test_file.txt", 'rt')
count = 0
word_count = 0
line = fh.readline()
unique_data = [{}]
while line:
    # do stuff with line
    string_line = line.strip()
    line = string_line.translate(string.maketrans("",""),  string.punctuation)
    line = line.lower()
    list_data = []
    list_data = line.split(" ")
    for item in list_data:
        if item == '':
            continue
        if item not in unique_data[0]:
            unique_data[0][item] = 1
            word_count = word_count + 1
        else:
            unique_data[0][item] = unique_data[0][item] + 1
    count = count + 1
    line = fh.readline()
"""
print unique_data[0]
print "Number of Words:" + str(word_count)
print str(len(unique_data[0])) 
print "Number of Lines:" + str(count) 
"""
fh.close()

plotting = []
plotting2 = []
#print unique_data[0]

# sorted(d, key=d.get)
#print sorted(unique_data[0],  key=unique_data[0].get )
#print unique_data[0]

#OrderedDict(sorted(d.items(), key=lambda t: t[0]))
unique_data[0] = collections.OrderedDict(sorted(unique_data[0].items(), key=lambda t: t[0]))
print unique_data[0]

for key in unique_data[0]:
    if unique_data[0][key] >= 50:
        plotting.append(unique_data[0][key])
        plotting2.append(unique_data[0][key] + random.randint(0, 100))

lines = plt.plot(plotting,  'ro-',  plotting2,  'g^-')
#plt.setp(lines,  linewidth=2, color='r')
plt.axis([0, len(plotting) + 10,  0, 2800])
#plt.ylabel('Number of word occured ')
#plt.xlabel('Word in the ')
plt.show()



#def function_name (*filename):
	#for fileInfo in filename:
		#print fileInfo
		

#function_name("Filename",'Information',['1','2','Ahmed'],{'Key':'Value','Name':'Ahmed'},5,6,"MyName")


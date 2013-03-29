import string
#string_line = "This is a line with information and has different chars, also we need to put them in a Dictionary, so that we can analyze them!"
file = open("test_file.txt", "rb")
string_line = file.readline() 
string_line = string_line.strip()
print string_line

line = string_line.translate(string.maketrans("",""),  string.punctuation)
list_data = []
list_data = line.split(" ")
print list_data

unique_data = dict()

for item in list_data:
    if item not in unique_data:
        unique_data[item] = 1
    else:
        unique_data[item] = unique_data[item] + 1

print unique_data
file.close()

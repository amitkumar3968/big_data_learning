import nltk   
import string
from urllib import urlopen

def FileSplitterToWordsPlain(file_name, file_type):
	# Creating Dictionary to store out unique word data
	unique_data = {}
	
	# Lets open the file and start reading it.
	if file_type == "plain":
		file_handler = open (file_name, "r+")
		line_feed = file_handler.readline()
	
	elif file_type == "html":
		line_feed = file_name
	
	#while line_feed:
		# Feeding line to strip and spaces
		string_line_feed = line_feed.strip()
		
		# Remove all special char from the line
		line_feed = string_line_feed.translate(string.maketrans("",""),  string.punctuation)
		
		# Change all the letters to Lowercase
		line_feed = line_feed.lower()
		
		# Split line into single token of words
		# above line will be as ["Split","line","into"] soon
		list_data = []
		list_data = line_feed.split(" ")
		
		# Now lets traverse though the list and add data to Dictionary
		for item in list_data:
			# if we enconter a blank '' then lets continue to next word
			if item == '' or item == '\t':
				continue
			# if 'word' is NOT present in the dictionary then its the first time
			# add the item with one	
			if item not in unique_data:
				unique_data[item] = 1
			# if 'word' was already in the dict() then increment Count
			else:
				unique_data[item] = unique_data[item] + 1
		# Now read the next line and feed it to 'while'
		#line_feed = file_handler.readline()
		
	# Close file and return data
	#file_handler.close()
	return unique_data






url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"    
html = urlopen(url).read()   
raw = nltk.clean_html(html)  
print raw
#print FileSplitterToWordsPlain(raw, "html")

"""
	This File Analysis multiple files and compares word usage count
"""

import string
import collections
import matplotlib.pyplot as plt
import sys

# File Type information.
FILE_TYPE_XML = "xml"
FILE_TYPE_CSV = "csv"
FILE_TYPE_JSON = "json"
FILE_TYPE_PLAIN_TEXT = "plain"
FILE_TYPE_HTML = "html"

"""
	DataReader Class does reading data and processing it.
"""
class DataReader:

	def __init__(self, *file_name_dictionary):
		self.file_name_dictionary = file_name_dictionary

	def FileSplitterToWordsPlain(self, file_name, file_type):
		# Creating Dictionary to store out unique word data
		unique_data = {}

		# Lets open the file and start reading it.
		if file_type == "plain":
			file_handler = open (file_name, "r+")
			line_feed = file_handler.readline()

		else:
			file_handler = file_name
			line_feed = file_handler.readline()

		while line_feed:
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
				if item == '':
					continue
				# if 'word' is NOT present in the dictionary then its the first time
				# add the item with one
				if item not in unique_data:
					unique_data[item] = 1
				# if 'word' was already in the dict() then increment Count
				else:
					unique_data[item] = unique_data[item] + 1
			# Now read the next line and feed it to 'while'
			line_feed = file_handler.readline()

		# Close file and return data
		file_handler.close()
		return unique_data

	# TODO
	def FileSplitterSpecialCharData(self):
		return None

	# TODO
	def FileOutputForProcessing(self):
		return None

	# Debugging
	def printDictionaryData(self, dictionary):
		for info_dict in dictionary:
			for info_key in info_dict:
				print "Key:", info_key

	def DataReaderBasedOnFileType(self):
		# Dictionary will contain data from multiple files
		output_data_list_dictionary = []

		# Lets Traverse through the Dictionary for different Files
		for file_info_dict in self.file_name_dictionary:
			for file_info_key in file_info_dict:

				# CSV file Analysis TODO
				if file_info_dict[file_info_key] == "csv":
					print "Lets Do something About this"
					continue

				# XML file Analysis TODO
				elif file_info_dict[file_info_key] == "xml":
					continue

				# json file Analysis TODO
				elif file_info_dict[file_info_key] == "json":
					continue

				# html file Analysis
				elif file_info_dict[file_info_key] == "html":
					url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
					html = urlopen(url).read()
					raw = nltk.clean_html(html)
					output_data_list_dictionary.append(self.FileSplitterToWordsPlain(raw, file_info_dict[file_info_key]))


				# plain text file Analysis
				elif file_info_dict[file_info_key] == "plain":
					# For Debugging
					#print "file_name", file_info_key, "file_type", file_info_dict[file_info_key]

					# Once data is returned from the Slipper Function we add it to the list.l
					output_data_list_dictionary.append(self.FileSplitterToWordsPlain(file_info_key, file_info_dict[file_info_key]))

					# For Debugging
					#print output_data_list_dictionary
					#print "Lets work on Plain Text"

				# Do nothing
				else:
					print "Cannot Process this file"
					continue
		return output_data_list_dictionary


"""
	Data Analysis and plotting
"""

class DataAnalysis:
	def __init__(self, data_analysis):
		# data we get is list of dictionaries [{},{},{}]
		self.data_analysis = data_analysis

	def printOuputData(self):
		for information in self.data_analysis:
			print information

	def plotDataForAnalysis(self):

		# Plotting data as a list list [[graph1],[graph2],[graph3]]
		plotting_data = []
		sorted_data = []

		# Sort each dictionary data in the list
		for data_in_dict in self.data_analysis:
			sorted_data.append(collections.OrderedDict(sorted(data_in_dict.items(), key=lambda t: t[0])))

		# Now for each dictionary let add data to a temp list
		for dictionary in sorted_data:
			plotting = []
			for items in dictionary:
				if dictionary[items] >= 50:
					plotting.append(dictionary[items])

			# Lets put all the plotting data back into the list
			plotting_data.append(plotting)
		#print plotting_data
		return plotting_data

	def plottingGraphData(self, plotting_data):
		# Traverse through the list to generate graph
		for information in plotting_data:
			plt.plot(information)
		plt.show()

if __name__ == '__main__':

    cmd_arguments = sys.argv
    file_dict = {}

    if len(cmd_arguments) >= 3:
        for item_file_name in cmd_arguments:
            if item_file_name == "two_file_analysis.py":
                continue
            else:
                file_dict[item_file_name] = FILE_TYPE_PLAIN_TEXT
        data_reader = DataReader(file_dict)
        dictionary_output = data_reader.DataReaderBasedOnFileType()

        data_analysis = DataAnalysis(dictionary_output)
        data_analysis.plottingGraphData(data_analysis.plotDataForAnalysis())
    else:
        data_reader = DataReader({"4.txt":FILE_TYPE_PLAIN_TEXT, "3.txt":FILE_TYPE_PLAIN_TEXT})
        dictionary_output = data_reader.DataReaderBasedOnFileType()

        data_analysis = DataAnalysis(dictionary_output)
        data_analysis.plottingGraphData(data_analysis.plotDataForAnalysis())


def function_name (*filename):
	for fileInfo in filename:
		for fileItem in fileInfo:
			print fileItem, fileInfo[fileItem]
	
	
def plotDataForAnalysis(data_analysis):
	plotting_data = []
	sorted_data = []
	#unique_data = collections.OrderedDict(sorted(unique_data[0].items(), key=lambda t: t[0]))
	for data_in_dict in data_analysis:
		sorted_data.append(collections.OrderedDict(sorted(data_in_dict.items(), key=lambda t: t[0])))
	
	for dictiondary in sorted_data:
		plotting = []
		for items in dictionary:
			plotting.append(dictionay[items])
		plotting_data.append(plotting)
	print plotting_data
		


data_dict = [{"filename": 122,"filename2":1,"filename3":4,"filename4":8},{"filename": 2,"filename2":1,"filename3":4564,"filename4":8},{"filename": 2123,"filename2":1231,"filename3":4,"filename4":123}]

plotDataForAnalysis(data_dict)

function_name({"filename":"type","filename2":"type","filename3":"type","filename4":"type"})

data = []
data.append({"filename":"type","filename2":"type","filename3":"type","filename4":"type"})
data.append({"filename":"type","filename2":"type","filename3":"type","filename4":"type"})
data.append({"filename":"type","filename2":"type","filename3":"type","filename4":"type"})
data.append({"filename":"type","filename2":"type","filename3":"type","filename4":"type"})

print data


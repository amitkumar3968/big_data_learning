import collections
import matplotlib.pyplot as plt

def plotDataForAnalysis(data_analysis):
	plotting_data = []
	sorted_data = []
	#unique_data = collections.OrderedDict(sorted(unique_data[0].items(), key=lambda t: t[0]))
	for data_in_dict in data_analysis:
		sorted_data.append(collections.OrderedDict(sorted(data_in_dict.items(), key=lambda t: t[0])))
	
	for dictionary in sorted_data:
		plotting = []
		for items in dictionary:
			plotting.append(dictionary[items])
		plotting_data.append(plotting)
	print plotting_data
	return plotting_data
		


data_dict = [{"filename": 1322,"filename2":3451,"filename3":3450,"filename4":3458},{"filename": 3442,"filename2":3431,"filename3":4564,"filename4":3450},{"filename": 2123,"filename2":1231,"filename3":1234,"filename4":1230}]
returned_data = plotDataForAnalysis(data_dict)

plt.plot([3442, 3431, 4564, 3450])
plt.plot([3450, 3331, 4764, 4564])
plt.plot([3442, 4564, 4564, 4564])
plt.plot([4564, 3431, 4564, 4564])

#plt.setp(lines,  linewidth=2, color='r')
#plt.ylabel('Number of word occured ')
#plt.xlabel('Word in the ')
plt.show()

import json
import csv
from numpy import genfromtxt
import random

def RBSNodeData(StationId, Status, AverageUAS, 
		AverageSES, AverageES, AverageAIS, 
		AverageRLTS1, AverageRLTS2, AverageRLTMMIN, 
		AverageRLTMMAX, TypeInfo):	
	RBSNode = {}
	RBSNode["StationId"] = StationId 
	RBSNode["Status"] = Status 
	RBSNode["AverageUAS"] = AverageUAS 
	RBSNode["AverageSES"] = AverageSES 
	RBSNode["AverageES"] = AverageES 
	RBSNode["AverageAIS"] = AverageAIS 
	RBSNode["AverageRLTS1"] = AverageRLTS1 
	RBSNode["AverageRLTS2"] = AverageRLTS2 
	RBSNode["AverageRLTMMIN"] = AverageRLTMMIN 
	RBSNode["AverageRLTMMAX"] = AverageRLTMMAX 
	RBSNode["type"] = TypeInfo 
	
	return RBSNode

def MWRNodeData(StationId, Status, PeakUtilizationTx, 
	PeakUtilizationRx, AverageThroughPutTx, AverageThroughPutRx, 
	AverageDropEvents, AverageCRCAlignError, AverageJabber, 
	AverageCollision, TypeInfo):
	
	MWRNode = {}				
						
	MWRNode["StationId"] =  StationId
	MWRNode["Status"] = Status 
	MWRNode["PeakUtilizationTx"] = PeakUtilizationTx 
	MWRNode["PeakUtilizationRx"] = PeakUtilizationRx
	MWRNode["AverageThroughPutTx"] = AverageThroughPutTx
	MWRNode["AverageThroughPutRx"] = AverageThroughPutRx
	MWRNode["AverageDropEvents"] = AverageDropEvents
	MWRNode["AverageCRCAlignError"] = AverageCRCAlignError
	MWRNode["AverageJabber"] =  AverageJabber
	MWRNode["AverageCollision"] = AverageCollision
	MWRNode["type"] = TypeInfo
	
	return MWRNode 

 
def NodeInfo(PhyAddress, SiteName, NodeData):

	checkIp = PhyAddress.split(".")
	if checkIp[3] == "1":
		Node = {}
		Node["id"] = PhyAddress
		Node["name"] = SiteName
		NodeData = {}
		NodeData["type"] = "router"
		NodeData["Status"] = "Present"
		Node["data"] = NodeData
		Node["children"] = []
	else:
		Node = {}
		Node["id"] = PhyAddress
		Node["name"] = SiteName
		Node["data"] = NodeData
		Node["children"] = []
		
	return Node
	
	
def addingChildren(ParentNode, Child):
	ParentNode["children"].append(Child)
	return ParentNode


"""
Write data to file - we write each line at a time.
"""
		
def write_string_to_file(file_name, string_to_write):
	# Open file in Append mode we want this as we will 
	# write multiple time in the same file.
	file_description = open(file_name, "w+")
	
	# Write line to File
	file_description.write(string_to_write)
	
	# Safely close file now.
	file_description.close()

def main():
	
	unique_ip = {}
	dictionary_node = {}
	data2 = []
	root = {}
	
	data = genfromtxt(open('input_tree.csv'), delimiter=',', dtype=None)
	for dataInfo in data:
		#print dataInfo
		if dataInfo[0] not in unique_ip:
			if dataInfo[0] == '':
				unique_ip[dataInfo[1]]="router"
			else:
				unique_ip[dataInfo[0]]=dataInfo[2]			
	
	#print unique_ip		
			
	for item in unique_ip:
		if unique_ip[item] == "MWR":
			name = item.split(".")
			MWRNode = MWRNodeData("CEBDH"+name[3]+"BEN DASH", "Present", 
						random.randrange(50000,100000), 
						random.randrange(25000,150000), 
						random.randrange(0,150),
						random.randrange(0,175),
						random.randrange(0,15),
						random.randrange(0,10),
						random.randrange(0,9),
						random.randrange(0,50),"MWR")
			data2.append(NodeInfo(item, "CEBDH7"+name[3], MWRNode))
		elif unique_ip[item] == "RBS":
			
			UAS = random.randrange(0,2)
			SES = random.randrange(0,2)
			ES = random.randrange(0,2)
			AIS = random.randrange(0,2)
			RLTS1 = random.randrange(0,2)
			RLTS2 = random.randrange(0,2)
			RLTM_MIN = random.randrange(-50, -45)
			RLTM_MAX = random.randrange(-44, -40)
						
			name = item.split(".")
			RBSNode = RBSNodeData("CE0"+name[3]+"BEN DASH", "Present", 
				UAS, SES, ES, AIS, RLTS1, RLTS2, 
				RLTM_MIN, RLTM_MAX, "RBS")
			data2.append(NodeInfo(item, "CEBDH70"+name[3], RBSNode))
		elif unique_ip[item] == "router":
			MWRNode = MWRNodeData("CEBDH BEN DASH", "Present", 
				0, 0, 0, 0, 0, 0, 0 , 0,"")
			name = item.split(".")
			data2.append(NodeInfo(item, "CEBDH70"+name[3], MWRNode))

	for item in data2:
		dictionary_node[item['id']] = item
	#print dictionary_node
	
	
	for tree in data:
		if tree[0] != '' and tree[1] != '':
			addingChildren(dictionary_node[tree[0]], 
				dictionary_node[tree[1]])
		elif tree[0] == '':
			print tree[1]   
			root = dictionary_node[tree[1]]
	
	write_string_to_file("Tree.json", json.dumps(root))
	print  json.dumps(root)

if __name__ == '__main__':
	main()





"""
CSV File Generator
	- Data is created as for each cluster.
	- Data is create as per the range of IP and Dates

"""

import csv 									
import random								
from datetime import date
from dateutil.rrule import rrule, DAILY
import os.path
import sys

"""
Init Data for generating Data
"""
my_data_header = "IPAddress,Date,Time,CustomerId,EqType,Interface,Status,PeakUtilizationTx,PeakUtilizationRx,ThroughputIn,ThroughputOut,DropEvents,OctetsRxTx,PacketsRxTx,BroadcastPktsRxTx,McastPktsRxTx,CRCAlignErrors,UndersizePkts,OversizePkts,Fragments,Jabbers,Collisions" + "\n"

cmd_arguments = sys.argv
print cmd_arguments

if len(cmd_arguments) > 1:
	if cmd_arguments[1] == "--low" or cmd_arguments[1] == "-l":
		cluster_ip = ["10.15.244.0", "10.15.243.0"] 			# Cluster Name - /24 based network - each cluster can have atmost 254 nodes
		interface = ["LAN-1","LAN-2","LAN-3","LAN-4","Port-A"] 	# Interface information 
		ip_start_range = 10										# IP x.x.x.12 start range, x.x.x. is replaced by the cluster IP info
		ip_end_range = 12										# IP x.x.x.13 end range, x.x.x. is replaced by the cluster IP info
		start_date = date(2013, 1, 1)							# Start date yyyy,mm,dd
		end_date = date(2013, 2, 1) 							# End date yyyy,mm,dd
		frequency = 1 											# Every hour data collection frequency 
	elif cmd_arguments[1] == "--medium" or cmd_arguments[1] == "-m":
		cluster_ip = ["10.15.244.0", "10.15.243.0","10.15.242.0"] 			
		interface = ["LAN-1","LAN-2","LAN-3","LAN-4","Port-A"] 	
		ip_start_range = 10										
		ip_end_range = 40										
		start_date = date(2013, 1, 1)							
		end_date = date(2013, 4, 1)								
		frequency = 1	
	elif cmd_arguments[1] == "--high" or cmd_arguments[1] == "-h":
		cluster_ip = ["10.15.244.0", "10.15.243.0", "10.15.242.0", "10.15.241.0"]
		interface = ["LAN-1","LAN-2","LAN-3","LAN-4","Port-A"] 	
		ip_start_range = 10										
		ip_end_range = 60										
		start_date = date(2013, 1, 1)							
		end_date = date(2013, 7, 1)								
		frequency = 1
else:
	cluster_ip = ["10.15.244.0", "10.15.243.0"] 			
	interface = ["LAN-1","LAN-2","LAN-3","LAN-4","Port-A"] 	
	ip_start_range = 10										
	ip_end_range = 12										
	start_date = date(2012, 5, 30)							
	end_date = date(2012, 9, 2)								
	frequency = 1


"""
Generating IP Range from Cluster IP information.
"""

def generate_ip_range(cluster_ip, start_ip, end_ip):
	# Sliptting Cluster IP information @ '.' so for IP 192.168.123.12 we get ['192', '168', '123', '12'] tuples
	cluster_ip_split = cluster_ip.split('.')
	
	# Create a list to have a list of IP range 
	ip_list = []
	
	# Start and end ip information from the Init Values
	if start_ip < end_ip:
		while start_ip <= end_ip:
			# Create a string of IP and append it to the ip_list list so that we can use it later.
			ip_list.append(str(cluster_ip_split[0])+"."+str(cluster_ip_split[1])+"."+str(cluster_ip_split[2])+"."+str(start_ip))
			start_ip = start_ip + 2
	return ip_list


"""
Generating Date Range - takes input as 'datetime.date(2012,12,23)' using 'datetime' library 
"""

def generate_date_range(start_date, end_date):

	# Creating a Date range using datetime library
	date_range = []
	for date_input in rrule(DAILY, dtstart=start_date, until=end_date):
		
		# we traverse through the date till we reach the end and append data to date_range list
		date_range.append(date_input.strftime("%Y-%m-%d"))

	return date_range
	

"""
Generating Data for every day / IP / Interface
"""

def generate_data_per_day(ip_data, date_data, interface_data, frequency):	
	
	# Init Values for the information which goes into the CSV file
	
	ip_address = ip_data
	date_time = date_data
	equipment_type = "ALFOplus80"
	customer_id = equipment_type + "_LOC_" + ip_address
	status = "OK"
	peak_utilization_tx = 0 	#random.randint(10000000:20000000) 
	peak_utilization_rx = 0 	#random.randint(10000000:20000000)
	throughput_in =  0 			#random.randint(10000000:20000000) * 8 / 1000000
	throughput_out = 0 			#random.randint(10000000:20000000) * 8 / 1000000
	drop_event = 0 				#random.randrange(50,100)
	octets_rx_tx = "NA"
	packets_rx_tx = "NA"
	broadcast_pkts_rx_tx = "NA"
	m_cast_pkts_rx_tx = "NA"
	crc_alignment_error = 0 	#random.randrange(10,20)
	undersize_pkts = "NA"
	oversize_pkts = "NA"
	fragmentation_count = 0 	#random.randrange(0,50)
	jabber_packets = 0 			#random.randrange(50,100)
	collisions = 0 				#random.randrange(0,20)

	# Init
	hour = 0
	
	# Creating a file_name using the IP information and Equipment Type
	file_name = equipment_type + "_LOC_" + ip_address + ".NM.csv"
	
	# Dont write to file if we are append to an exsisting file 
	# as this is just the header
	if os.path.isfile(file_name) != True:
		write_string_to_file(file_name, my_data_header)
	
	while hour != 24:
		
		# Generating random information in the values below
		peak_utilization_tx = random.randint(10000000,20000000) 
		peak_utilization_rx = random.randint(10000000,20000000)
		throughput_in =  random.randint(10000000,20000000) * 8 / 1000000
		throughput_out = random.randint(10000000,20000000) * 8 / 1000000
		drop_event = random.randrange(50,100)
		crc_alignment_error = random.randrange(10,20)
		fragmentation_count = random.randrange(0,50)
		jabber_packets = random.randrange(50,100)
		collisions = random.randrange(0,20)
		
		# Create a string to write to file, comma separated.
		string_to_file = ip_address + "," + date_time  + "," +  str(hour)+":00"  + "," + customer_id + "," +  equipment_type + "," +  interface_data + "," +  status + "," +  str(peak_utilization_tx) + "," + str(peak_utilization_rx) + "," + str(throughput_in) + "," + str(throughput_out) + "," + str(drop_event) + "," + octets_rx_tx + "," + packets_rx_tx + "," + broadcast_pkts_rx_tx + "," + m_cast_pkts_rx_tx + "," + str(crc_alignment_error) + "," + undersize_pkts + "," + oversize_pkts + "," + str(fragmentation_count) + "," + str(jabber_packets) + "," + str(collisions) + "\n"
		write_string_to_file(file_name, string_to_file)
		
		# Adding frequency as we can change this as required.
		hour = hour + frequency


"""
Write data to file - we write each line at a time.
"""
		
def write_string_to_file(file_name, string_to_write):
	# Open file in Append mode we want this as we will write multiple time in the same file.
	file_description = open(file_name, "a+")
	
	# Write line to File
	file_description.write(string_to_write)
	
	# Safely close file now.
	file_description.close()
	
	
"""
Main Function
"""
	
if __name__ == '__main__':
	
	# Start from the Cluster and traverse the cluster for cluster IP
	for cluster_info in cluster_ip:

		# Create a Range using the function which takes cluster_ip as the input
		range_ip = generate_ip_range(cluster_info, ip_start_range, ip_end_range)
		print "Generating files for Cluster : " + cluster_info
		
		# For every IP lets create a file
		for range_ip_info in range_ip:
			
			# Taking a range for Interface information from the init value list
			for interface_type_range in range(0,5): 
				
				# Now lets generate the date range to write to file using init values above
				range_date = generate_date_range(start_date,end_date)
				for range_date_info in range_date:
					# print range_ip_info, range_date_info, interface[interface_type_range], frequency
					# For date, IP, Interface we generate a file
					# Each file is unique for every IP within a Cluster
					generate_data_per_day(range_ip_info, range_date_info, interface[interface_type_range], frequency)
					# continue
		print "File Generation Complete for Cluster : " + cluster_info
	print "\n------------------------------------------"	
	print "File Generation Complete for ALL Clusters"			


"""
CSV File Generator
	- Data is created as for each cluster.
	- Data is create as per the range of IP and Dates

"""

import csv 									
import random								
from datetime import date
import datetime
from dateutil.rrule import rrule, DAILY
import os.path
import sys

"""
Init Data for generating Data
"""
#my_data_header = "IP-Address,Date&Time,CustomerId,Eq.Type,Interface,Status,Drop Events,Octets RX,Pkts RX,Broadcast Pkts RX,Multicast Pkts RX,CRC Align Error,Undersize Pkts,Oversize Pkts,Fragments,Jabber,Collisions,Utilization RX,Octets TX,Pkts TX,Broadcast Pkts TX,Multicast Pkts TX,Utilization TX,Min Bandwidth (Mbits/s),Max Bandwidth (Mbits/s)" + "\n"
my_data_header  = "NE Identifier,IPAddress,Date&Time,NE Type,Radio Branch Id,PMStatus,UAS,SES,ES,AIS,RLTS1,RLTS2,RLTM MIN,RLTM MAX,TLTM MIN,TLTM MAX" + "\n"


cmd_arguments = sys.argv
print cmd_arguments


if len(cmd_arguments) > 1:
	if cmd_arguments[1] == "--low" or cmd_arguments[1] == "-l":
		cluster_ip = ["10.15.244.0", "10.15.243.0"] 			# Cluster Name - /24 based network - each cluster can have atmost 254 nodes
		radio_branch_id = ["1A","2A"] 	# radio_branch_id information 
		ip_start_range = 10										# IP x.x.x.12 start range, x.x.x. is replaced by the cluster IP info
		ip_end_range = 12										# IP x.x.x.13 end range, x.x.x. is replaced by the cluster IP info
		start_date = date(2013, 1, 1)							# Start date yyyy,mm,dd
		end_date = date(2013, 2, 1) 							# End date yyyy,mm,dd
		frequency = 900											# Data collection frequency in Seconds (900 == 15 minutes)
		day_in_seconds = 86400
		day_9_45_am = 35100 
	elif cmd_arguments[1] == "--medium" or cmd_arguments[1] == "-m":
		cluster_ip = ["10.15.244.0", "10.15.243.0","10.15.242.0"] 			
		radio_branch_id = ["1A","2A"] 	
		ip_start_range = 10										
		ip_end_range = 40										
		start_date = date(2013, 1, 1)							
		end_date = date(2013, 4, 1)								
		frequency = 900	
		day_in_seconds = 86400
		day_9_45_am = 35100 
	elif cmd_arguments[1] == "--high" or cmd_arguments[1] == "-h":
		cluster_ip = ["10.15.244.0", "10.15.243.0", "10.15.242.0", "10.15.241.0"]
		radio_branch_id = ["1A","2A"] 	
		ip_start_range = 10										
		ip_end_range = 60										
		start_date = date(2013, 1, 1)							
		end_date = date(2013, 7, 1)								
		frequency = 900
		day_in_seconds = 86400
		day_9_45_am = 35100 
	elif cmd_arguments[1] == "--vlow" or cmd_arguments[1] == "-vl":
		cluster_ip = ["10.15.244.0"]
		radio_branch_id = ["1A","2A"] 	
		ip_start_range = 10										
		ip_end_range = 12										
		start_date = date(2013, 1, 1)							
		end_date = date(2013, 1, 1)								
		frequency = 900
		day_in_seconds = 36000
		day_9_45_am = 35100 
else:
	cluster_ip = ["10.15.244.0", "10.15.243.0"] 			
	radio_branch_id = ["1A","2A"] 	
	ip_start_range = 10										
	ip_end_range = 12										
	start_date = date(2012, 5, 30)							
	end_date = date(2012, 9, 2)								
	frequency = 900
	day_in_seconds = 86400
	day_9_45_am = 35100 


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
		date_range.append(date_input.strftime("%d%m%y"))

	return date_range
	

"""
Generating Data for every day / IP / radio_branch_id
"""

def generate_data_per_day(ip_data, date_data, radio_branch_id_data, frequency):	
	
	# Init Values for the information which goes into the CSV file
	ip_address = ip_data
	NE_Identifier = "CE002700_" + ip_address
	date_time = date_data
	NE_type = "ALCplus2"
	status = "On"
	UAS = 0
	SES = 0
	ES = 0
	AIS = 0
	RLTS1 = 0
	RLTS2 = 0
	RLTM_MIN = 0 
	RLTM_MAX = 0
	TLTM_MIN = 0
	TLTM_MAX = 0
	

	# Init
	second = 0
	
	# Creating a file_name using the IP information and Equipment Type
	file_name = "MWRRadioPerformaceReport" + ip_address + ".csv"
	
	# Dont write header data to file, if we are append to an exsisting file 
	if os.path.isfile(file_name) != True:
		write_string_to_file(file_name, my_data_header)
	
	# Till we reach end of day - 86400 seconds == 24 hours
	while second != day_in_seconds:
		
		# Generating random information in the values below
		UAS = random.randrange(0,2)
		SES = random.randrange(0,2)
		ES = random.randrange(0,2)
		AIS = random.randrange(0,2)
		RLTS1 = random.randrange(0,2)
		RLTS2 = random.randrange(0,2)
		RLTM_MIN = random.randrange(-50, -45)
		RLTM_MAX = random.randrange(-44, -40)
		TLTM_MIN = random.randrange(18,25)
		TLTM_MAX = random.randrange(18,25)
		
		# Create a string to write to file, comma separated.
		
		# when we below 35100 it is 9:45 but we need 09:45 and then we do a split to get 0945
		if second <= day_9_45_am:
			time_print = str(datetime.timedelta(seconds=second))[:4]
			time_new = time_print.split(":")
			time_new = time_new[0] + time_new[1]
			#               "NE Identifier,        IPAddress,         Date&Time,                             NE Type,       Radio Branch Id,          PMStatus,        UAS,              SES,              ES,               AIS,           RLTS1,               RLTS2,             RLTM MIN,             RLTM MAX,             TLTM MIN,             TLTM MAX"
			string_to_file = NE_Identifier + "," + ip_address + "," + date_time  + ":0" +  time_new + "," + NE_type + "," +  radio_branch_id_data + "," +  status + "," +  str(UAS) + "," +  str(SES) + "," + str(ES) + "," + str(AIS) + "," + str(RLTS1) + "," + str(RLTS2) + "," + str(RLTM_MIN) + "," + str(RLTM_MAX) + "," + str(TLTM_MIN) + "," + str(TLTM_MAX) + "\n"
			write_string_to_file(file_name, string_to_file)
			
		# else we are good to print time as it is
		else:
			time_print = str(datetime.timedelta(seconds=second))[:5]
			time_new = time_print.split(":")
			time_new = time_new[0] + time_new[1]
			#               "NE Identifier,        IPAddress,         Date&Time,                             NE Type,       Radio Branch Id,          PMStatus,        UAS,              SES,              ES,               AIS,           RLTS1,               RLTS2,             RLTM MIN,             RLTM MAX,             TLTM MIN,             TLTM MAX"
			string_to_file = NE_Identifier + "," + ip_address + "," + date_time  + ":" +  time_new + "," + NE_type + "," +  radio_branch_id_data + "," +  status + "," +  str(UAS) + "," +  str(SES) + "," + str(ES) + "," + str(AIS) + "," + str(RLTS1) + "," + str(RLTS2) + "," + str(RLTM_MIN) + "," + str(RLTM_MAX) + "," + str(TLTM_MIN) + "," + str(TLTM_MAX) + "\n"
			write_string_to_file(file_name, string_to_file)
		# Adding frequency which is in Seconds, and we can change this as required.
		second = second + frequency


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
			
			# Taking a range for radio_branch_id information from the init value list
			for radio_branch_id_type_range in range(0,2): 
				
				# Now lets generate the date range to write to file using init values above
				range_date = generate_date_range(start_date,end_date)
				for range_date_info in range_date:
					# print range_ip_info, range_date_info, radio_branch_id[radio_branch_id_type_range], frequency
					# For date, IP, radio_branch_id we generate a file
					# Each file is unique for every IP within a Cluster
					generate_data_per_day(range_ip_info, range_date_info, radio_branch_id[radio_branch_id_type_range], frequency)
					# continue
		print "File Generation Complete for Cluster : " + cluster_info
	print "\n------------------------------------------"	
	print "File Generation Complete for ALL Clusters"			


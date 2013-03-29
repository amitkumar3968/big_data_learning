import csv
import MySQLdb
import os

file_directory_path = "/home/ahmed/test_dir"

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='mydb')
cursor = mydb.cursor()

file_list = []
file_list = os.listdir(file_directory_path)

for file_names in file_list:
	if file_names[-7:] == ".NM.csv":
		csv_data = csv.reader(file(file_names))
		for row in csv_data:
			cursor.execute('INSERT INTO testcsv(IPAddress,Date,Time,CustomerId,EqType,Interface,Status,PeakUtilizationTx,PeakUtilizationRx,ThroughputIn,ThroughputOut,DropEvents,OctetsRxTx,PacketsRxTx,BroadcastPktsRxTx,McastPktsRxTx,CRCAlignErrors,UndersizePkts,OversizePkts,Fragments,Jabbers,Collisions) '\
			'VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s","%s", "%s","%s", "%s","%s", "%s","%s", "%s","%s", "%s")', row)
		mydb.commit()
	else:
		print "Skipping file :" + file_names
		
#close the connection to the database.
cursor.close()
print "Done"

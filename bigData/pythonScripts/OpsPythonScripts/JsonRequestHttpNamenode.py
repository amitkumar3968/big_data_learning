#!/usr/bin/python

import urllib
import json
import os

# This will help display 5 chars
# 10.23764523674 will be displayed as 10.23
decimalLimit=5

# Executing system command
def commandExecutor(command):
    # Executing generated shell script on the server.
    response = os.system(command)

    # If we get 0, then all is well.
    if response == 0:
        print "Execution Successful"


# Setting up email Notification
def settingMailingInfo(memoryDataDictionary, currentStatus):

    # We send the email to ti_operation else we dont need to.
    # Checking for STATUS.

    if currentStatus == "RED":
        # Creating a Shell based string which will be executing using the os.system commands above.
        emailNotification = "echo -e \"Hi Team,\\n\\nBelow are the Details about Namenode Heap Memory" \
                 "\\n\\nCommitted Heap Memory (%) : "+str(memoryDataDictionary["committedHeapPercentage"])[:decimalLimit]+"%\\n" \
                 "Used Heap Memory (%) : "+str(memoryDataDictionary["usedHeapPercentage"])[:decimalLimit]+"%\\n\\n" \
                 "Max Heap Memory : "+str(memoryDataDictionary["maxHeap"])[:decimalLimit]+" GB\\n" \
                 "Used Heap Memory : "+str(memoryDataDictionary["usedHeap"])[:decimalLimit]+" GB\\n" \
                 "Committed Heap Memory : "+str(memoryDataDictionary["committedHeap"])[:decimalLimit]+" GB\\n\\n" \
                 "Current Status is : "+str(currentStatus)+"\\n\\n" \
                 "IMPORTANT : If we see Committed Heap Memory (%) goes above 85% then we need to prepare for Namenode restart." \
                 "Currently Namenode is running on prod-master2. \\n\\n" \
                 "Below are the necessary steps to be taken for Namenode (NN) restart\\n" \
                 "\\t 1. Check if no job is running on the Cluster. http://prod-master1:50070/dfshealth.jsp \\n" \
                 "\\t 2. Login to prod-master2. \\n" \
                 "\\t 3. Check for current status of NN >> 'sudo service hadoop-hdfs-namenode status' \\n" \
                 "\\t 4. Restarting NN >> 'sudo service hadoop-hdfs-namenode restart'\\n" \
                 "\\t NOTE. One way to check if NN restarted, is to check the PID of NN before and after the restart.\\n" \
                 "\\nBest Regards,\\nTI Operations Team\\n\\n--\\nPlease do not respond to this mail. " \
                 "For any queries Contact ti_operations@saggezza.com\\n\\n\"" \
                 "| mailx -v -A gmail -s \"STATUS : "+currentStatus+" - Heap Memory @ "+str(memoryDataDictionary["committedHeapPercentage"])[:decimalLimit]+"% Current Time : $(date +%H:%M)\" ti_operations@saggezza.com"
    else:
        emailNotification = "echo -e \"Hi Team,\\n\\nBelow are the Details about Namenode Heap Memory" \
                 "\\n\\nCommitted Heap Memory (%) : "+str(memoryDataDictionary["committedHeapPercentage"])[:decimalLimit]+"%\\n" \
                 "Used Heap Memory (%) : "+str(memoryDataDictionary["usedHeapPercentage"])[:decimalLimit]+"%\\n\\n" \
                 "Max Heap Memory : "+str(memoryDataDictionary["maxHeap"])[:decimalLimit]+" GB\\n" \
                 "Used Heap Memory : "+str(memoryDataDictionary["usedHeap"])[:decimalLimit]+" GB\\n" \
                 "Committed Heap Memory : "+str(memoryDataDictionary["committedHeap"])[:decimalLimit]+" GB\\n\\n" \
                 "Current Status is : "+str(currentStatus)+"\\n\\n" \
                 "IMPORTANT : If we see Committed Heap Memory (%) goes above 85% then we need to prepare for Namenode restart." \
                 "Currently Namenode is running on prod-master2. \\n\\n" \
                 "Below are the necessary steps to be taken for Namenode(NN) restart\\n" \
                 "\\t 1. Check if no job is running on the Cluster. http://prod-master1:50070/dfshealth.jsp \\n" \
                 "\\t 2. Login to prod-master2. \\n" \
                 "\\t 3. Check for current status of NN >> 'sudo service hadoop-hdfs-namenode status' \\n" \
                 "\\t 4. Restarting NN >> 'sudo service hadoop-hdfs-namenode restart'\\n" \
                 "\\t NOTE. One way to check if NN restarted, is to check the PID of NN before and after the restart.\\n" \
                 "\\nBest Regards,\\nTI Operations Team\\n\\n--\\nPlease do not respond to this mail. " \
                 "For any queries Contact ti_operations@saggezza.com\\n\\n\"" \
                 "| mailx -v -A gmail -s \"STATUS : "+currentStatus+" - Heap Memory @ "+str(memoryDataDictionary["committedHeapPercentage"])[:decimalLimit]+"% Current Time : $(date +%H:%M)\" 'zubair.ahmed@saggezza.com,leo.bernardi@saggezza.com'"

    return emailNotification



# Get data from URL - JSON in our case.
def gettingDataFromURL():

    # Creating a Dictionary to hold all our data
    # Currently hold only Heap Memory
    heapDataDictionary = dict()

    # How we would like to show the Memory - Currently in GB
    GB = 1024 * 1024 * 1024
    MB = 1024 * 1024
    KB = 1024

    # Server URL to get JSON information
    url = 'http://prod-master1:50070/jmx'
    result = json.load(urllib.urlopen(url))

    # Heap Memory Info - Max, Used, Committed.
    heapDataDictionary["maxHeap"] = float(result["beans"][0]["HeapMemoryUsage"]["max"]) / GB
    heapDataDictionary["usedHeap"] = float(result["beans"][0]["HeapMemoryUsage"]["used"]) / GB
    heapDataDictionary["committedHeap"] = float(result["beans"][0]["HeapMemoryUsage"]["committed"]) / GB
    heapDataDictionary["initHeap"] = float(result["beans"][0]["HeapMemoryUsage"]["init"]) / GB

    # generating % for our values.
    heapDataDictionary["usedHeapPercentage"] = heapDataDictionary["usedHeap"] / heapDataDictionary["maxHeap"] * 100
    heapDataDictionary["committedHeapPercentage"] = heapDataDictionary["committedHeap"] / heapDataDictionary["maxHeap"] * 100

    return heapDataDictionary

if __name__=="__main__":

    # Getting information from the NN server.
    # Currently running on prod-master2
    memoryDataDictionary = gettingDataFromURL()

    # Setting Status
    _RED="RED"
    _YELLOW="YELLOW"
    _GREEN="GREEN"

    # If we are going above 80% then send a RED flag error.
    # We need to prepare for NN restart.

    # Below are the necessary steps to be taken for Namenode(NN) restart
    #     1. Check if no job is running on the Cluster.(http://prod-master1:50070/dfshealth.jsp)
    #        and Log on to prod-master1
    #     2. Check for current status of NN 'sudo service hadoop-hdfs-namenode status'
    #     3. Restarting NN 'sudo service hadoop-hdfs-namenode restart'
    #     NOTE. One way to check if NN restart is to check the PID of NN before and after the restart.


    if memoryDataDictionary["committedHeapPercentage"] > 80:
        email = settingMailingInfo(memoryDataDictionary, _RED)
        commandExecutor(email)
    elif memoryDataDictionary["committedHeapPercentage"] > 65 \
            and memoryDataDictionary["committedHeapPercentage"] < 80:
        email = settingMailingInfo(memoryDataDictionary, _YELLOW)
        commandExecutor(email)
    else:
        email = settingMailingInfo(memoryDataDictionary, _GREEN)
        commandExecutor(email)

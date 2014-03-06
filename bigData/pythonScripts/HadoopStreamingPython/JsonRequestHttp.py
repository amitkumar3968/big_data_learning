#!/usr/bin/python

import urllib
import json
import os

# This will help display 5 chars
# 10.23764523674 will be displayed as 10.23
decimalLimit=5

# Executing system command
def commandExecutor(command):
    response = os.system(command)
    if response == 0:
        print "Execution Successful"

# Setting up email Notification
def settingMailingInfo(memoryDataDictionary, currentStatus):

    print memoryDataDictionary
    emailNotification = "echo -e \"Hi Team,\\n\\nBelow are the Details about Job Tracker Heap Memory" \
             "\\n\\nCommitted Heap Memory : "+str(memoryDataDictionary["committedHeapPercentage"])[:decimalLimit]+"%\\n" \
             "Used Heap Percentage : "+str(memoryDataDictionary["usedHeapPercentage"])[:decimalLimit]+"%\\n\\n" \
             "Max Heap Memory : "+str(memoryDataDictionary["maxHeap"])+"\\n" \
             "Used Heap Memory : "+str(memoryDataDictionary["usedHeap"])+"\\n\\n" \
             "Committed Heap Memory : "+str(memoryDataDictionary["committedHeap"])+"\\n" \
             "Current Status is : "+str(currentStatus)+"\\n" \
             "\\nBest Regards,\\nTI Operations Team\\n\\n--\\nPlease do not respond to this mail. " \
             "For any queries Contact ti_operations@saggezza.com\\n\\n\" " \
             "| mailx -v -A gmail -s \"STATUS:"+currentStatus+" - Heap Memory Notification - Memory @ "+str(memoryDataDictionary["committedHeapPercentage"])[:decimalLimit]+"% Current Time : $(date +%H:%M)\" zubair.ahmed@saggezza.com"
    return emailNotification

# Get data from URL - JSON in our case.
def gettingDataFromURL():

    heapDataDictionary = dict()

    url = 'http://prod-master2:50030/jmx'
    result = json.load(urllib.urlopen(url))

    heapDataDictionary["maxHeap"] = float(result["beans"][1]["HeapMemoryUsage"]["max"])
    heapDataDictionary["usedHeap"] = float(result["beans"][1]["HeapMemoryUsage"]["used"])
    heapDataDictionary["committedHeap"] = float(result["beans"][1]["HeapMemoryUsage"]["committed"])

    heapDataDictionary["usedHeapPercentage"] = heapDataDictionary["usedHeap"] / heapDataDictionary["maxHeap"] * 100
    heapDataDictionary["committedHeapPercentage"] = heapDataDictionary["committedHeap"] / heapDataDictionary["maxHeap"] * 100

    return heapDataDictionary




if __name__=="__main__":
    memoryDataDictionary = gettingDataFromURL()

    _RED="RED"
    _YELLOW="YELLOW"
    _GREEN="GREEN"

    if memoryDataDictionary["committedHeapPercentage"] > 80:
        print memoryDataDictionary["committedHeapPercentage"]
        settingMailingInfo(memoryDataDictionary, _RED)
    elif memoryDataDictionary["committedHeapPercentage"] > 65 \
            and memoryDataDictionary["committedHeapPercentage"] < 80:
        print memoryDataDictionary["committedHeapPercentage"]
        settingMailingInfo(memoryDataDictionary, _YELLOW)
    else:
        print memoryDataDictionary["committedHeapPercentage"]
        email = settingMailingInfo(memoryDataDictionary, _GREEN)
        commandExecutor(email)

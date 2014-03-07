__author__ = 'ahmed'

#!/usr/bin/python

import urllib
import json
import os


# This will help display 5 chars
# 10.23764523674 will be displayed as 10.23
decimalLimit=5

# Some Constant for Error handling and threshold
ERROR = 999999
THRESHOLD = 85

def emailSubjectMessage(currentStatus, memoryInformation, serverName):
    subjectAndMailing = "| mailx -v -A gmail -s \"STATUS : "+currentStatus+" - Server Name : "+serverName+", Heap Memory @ "+memoryInformation+"\" zubair.ahmed@saggezza.com"
    return subjectAndMailing


def emailSubjectMessage():
    subjectAndMailing = "| mailx -v -A gmail -s \"Datanode (DN) Monitoring Service. Current Time : $(date +%H:%M)\" zubair.ahmed@saggezza.com"
    return subjectAndMailing


def emailBodyMessage(memoryDic):

    bodyMessage = ""
    for dataListOfDictionary in memoryDic:
        if not dataListOfDictionary == {}:
            bodyMessage = bodyMessage + "\"Server Name: " + dataListOfDictionary['serverUrl'] + "\\n" \
                        "Node Status : " + dataListOfDictionary['nodeStatus'] +"\\n"\
                        "Used Heap Memory (%) : " + dataListOfDictionary['usedHeapPercentage'] +"\\n"\
                        "Committed Heap Memory (%) : " + dataListOfDictionary['committedHeapPercentage'] +"\\n\\n\""

    return bodyMessage



def emailBodyFooter(aboutInfo):
    bodyFooter = "\"IMPORTANT : If we see Used Heap Memory (%) goes above 85% then we need to look into that specific "+aboutInfo+"." \
                 "\\n\\nBest Regards,\\nTI Operations Team\\n\\n--\\nPlease do not respond to this mail. " \
                 "For any queries Contact ti_operations@saggezza.com\\n\\n\""
    return bodyFooter


def emailBodyHeader(aboutInfo):
    bodyHeader = "echo -e \"Hi Team,\\n\\nBelow are the Details about "+aboutInfo+" Heap Memory\\n\\n\""
    return bodyHeader



# Executing system command
def commandExecutor(command):
    # Executing generated shell script on the server.
    response = os.system(command)

    # If we get 0, then all is well.
    if response == 0:
        print "Execution Successful"


# Get data from URL - JSON in our case.
def gettingDataFromURL(URL, heapMemoryIndex):

    if heapMemoryIndex < 0:
        print ("Enter Valid heapMemoryIndex, "
               "should be a number and should be 0 or above")
        return ERROR

    if URL == "":
        print("Please pass valid URL")
        return ERROR
    # Creating a Dictionary to hold all our data
    # Currently hold only Heap Memory
    heapDataDictionary = dict()

    # How we would like to show the Memory - Currently in GB
    GB = 1024 * 1024 * 1024
    MB = 1024 * 1024
    KB = 1024

    # Server URL to get JSON information
    result = json.load(urllib.urlopen(URL))

    # Heap Memory Info - Max, Used, Committed.
    heapDataDictionary["serverUrl"] = URL
    maxHeap = float(result["beans"][heapMemoryIndex]["HeapMemoryUsage"]["max"]) / GB
    usedHeap = float(result["beans"][heapMemoryIndex]["HeapMemoryUsage"]["used"]) / GB
    committedHeap = float(result["beans"][heapMemoryIndex]["HeapMemoryUsage"]["committed"]) / GB
    initHeap = float(result["beans"][heapMemoryIndex]["HeapMemoryUsage"]["init"]) / GB

    # generating % for our values.
    usedHeapPercentage = usedHeap / maxHeap * 100
    committedHeapPercentage = committedHeap / maxHeap * 100

    if usedHeapPercentage > THRESHOLD:
        heapDataDictionary["nodeStatus"] = "RED"
    elif usedHeapPercentage < THRESHOLD and usedHeapPercentage > 70:
        heapDataDictionary["nodeStatus"] = "YELLOW"
    else:
        heapDataDictionary["nodeStatus"] = "GREEN"

    heapDataDictionary["maxHeap"] = str(maxHeap)[:decimalLimit]
    heapDataDictionary["usedHeap"] = str(usedHeap)[:decimalLimit]
    heapDataDictionary["committedHeap"] = str(committedHeap)[:decimalLimit]
    heapDataDictionary["initHeap"] = str(initHeap)[:decimalLimit]

    # generating % for our values.
    heapDataDictionary["usedHeapPercentage"] = str(usedHeapPercentage)[:decimalLimit]+"%"
    heapDataDictionary["committedHeapPercentage"] = str(committedHeapPercentage)[:decimalLimit]+"%"

    return heapDataDictionary


def urlFromInput(serverName, listenPort):

    if listenPort < 0:
        print ("Enter Valid heapMemoryIndex, "
               "should be a number and should be 0 or above")
        return ERROR

    if serverName == "":
        print("Please pass valid URL")
        return ERROR

    URL = "http://"+serverName+":"+str(listenPort)+"/jmx"
    print(URL)
    return URL


if __name__=="__main__":

    serverList = ["prod-data1", "prod-data2", "prod-data3", "prod-data4", "prod-data5",
                  "prod-data6", "prod-data7", "prod-data8", "prod-data9", "prod-data10"]

    #serverList = ["prod-data1", "prod-data2"]

    portToQuery = 50075
    indexToQuery = 0

    dataListOfDictionary = []

    for serverName in serverList:
        getUrl = urlFromInput(serverName, portToQuery)
        if getUrl == ERROR:
            break
        heapDictionary = gettingDataFromURL(getUrl, indexToQuery)
        if heapDictionary == ERROR:
            break
        dataListOfDictionary.append(heapDictionary)

    headerEmailBody = emailBodyHeader("Datanode (DN)")
    footerEmailBody = emailBodyFooter("Datanode (DN)")
    subjectEmail = emailSubjectMessage()
    mainMessageEmailBody = emailBodyMessage(dataListOfDictionary)

    # Execute command to send all information as a mail
    commandExecutor(headerEmailBody + mainMessageEmailBody + footerEmailBody + subjectEmail)
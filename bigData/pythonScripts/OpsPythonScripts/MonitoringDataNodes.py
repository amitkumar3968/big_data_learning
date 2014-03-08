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

def emailSubjectMessageDetailed(currentStatus, memoryInformation, serverName):
    subjectAndMailing = "| mailx -v -A gmail -s \"STATUS : "+currentStatus+" - Server Name : "+serverName+", Used Heap Memory @ "+memoryInformation+"\" zubair.ahmed@saggezza.com"
    return subjectAndMailing


def emailSubjectMessage(serviceType):
    subjectAndMailing = "| mailx -v -A gmail -s \""+serviceType+" Monitoring Service. Current Time : $(date +%H:%M)\" zubair.ahmed@saggezza.com"
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

def emailBodyMessageDetailed(memoryDic, memMeasure):

    bodyMessage = ""
    for dataListOfDictionary in memoryDic:
        if not dataListOfDictionary == {}:
            bodyMessage = bodyMessage + "\"Server Name: " + dataListOfDictionary['serverUrl'] + "\\n" \
                        "Node Status : " + dataListOfDictionary['nodeStatus'] +"\\n"\
                        "Used Heap Memory (%) : " + dataListOfDictionary['usedHeapPercentage'] +"\\n"\
                        "Committed Heap Memory (%) : " + dataListOfDictionary['committedHeapPercentage'] +"\\n\\n"\
                        "Used Heap Memory : " + dataListOfDictionary['usedHeap'] +" "+memMeasure+"\\n"\
                        "Committed Heap Memory : " + dataListOfDictionary['committedHeap']+" "+memMeasure +"\\n"\
                        "Max Heap Memory : " + dataListOfDictionary['maxHeap']+" "+memMeasure +"\\n"\
                        "Init Heap Memory : " + dataListOfDictionary['initHeap']+" "+memMeasure +"\\n\\n\""

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

    # Exit Conditions
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


# This function converts the servername to URL which we need to query.
def urlFromInput(serverName, listenPort):

    if listenPort < 0:
        print ("Enter Valid heapMemoryIndex, "
               "should be a number and should be 0 or above")
        return ERROR

    if serverName == "":
        print("Please pass valid URL")
        return ERROR

    URL = "http://"+serverName+":"+str(listenPort)+"/jmx"
    return URL


if __name__=="__main__":

    # List of Nodes to Query
    serverList = ["prod-data1", "prod-data2", "prod-data3", "prod-data4", "prod-data5",
                  "prod-data6", "prod-data7", "prod-data8", "prod-data9", "prod-data10"]


    #############
    # DATANODE
    #############

    # Port which we need to query and
    # Index information on the JSON whic has the Heap Memory information
    portToQueryDataNode = 50075
    indexToQueryDataNode = 0

    # Dict to store all data.
    dataNodeListDictionary = []

    # Running through the list to create dictionary of information.
    for serverName in serverList:
        getUrl = urlFromInput(serverName, portToQueryDataNode)
        if getUrl == ERROR:
            continue
        heapDictionary = gettingDataFromURL(getUrl, indexToQueryDataNode)
        if heapDictionary == ERROR:
            continue
        dataNodeListDictionary.append(heapDictionary)

    if not dataNodeListDictionary == []:
        # Setting up Email Processing
        headerEmailBody = emailBodyHeader("Datanode (DN)")
        footerEmailBody = emailBodyFooter("Datanode (DN)")
        subjectEmail = emailSubjectMessage("Datanode (DN)")
        mainMessageEmailBody = emailBodyMessage(dataNodeListDictionary)

        # Execute command to send all information as a mail
        print(headerEmailBody + mainMessageEmailBody + footerEmailBody + subjectEmail)
    else:
        print "ERROR : Dictionary is Empty!!"

    #############
    # REGION SERVER
    #############

    # Port which we need to query and
    # Index information on the JSON whic has the Heap Memory information
    portToQueryRegionServer = 60030
    indexToQueryRegionServer = 1

    # Dict to store all data.
    regionServerListDictionary = []

    # Running through the list to create dictionary of information.
    for serverName in serverList:
        getUrl = urlFromInput(serverName, portToQueryRegionServer)
        if getUrl == ERROR:
            continue
        heapDictionary = gettingDataFromURL(getUrl, indexToQueryRegionServer)
        if heapDictionary == ERROR:
            continue
        regionServerListDictionary.append(heapDictionary)

    if not regionServerListDictionary == []:
        # Setting up Email Processing
        headerEmailBody = emailBodyHeader("HBase RegionServer")
        footerEmailBody = emailBodyFooter("Hbase RegionServer")
        subjectEmail = emailSubjectMessage("Hbase RegionServer")
        mainMessageEmailBody = emailBodyMessage(regionServerListDictionary)

        # Execute command to send all information as a mail
        print(headerEmailBody + mainMessageEmailBody + footerEmailBody + subjectEmail)
    else:
        print "ERROR : Dictionary is Empty!!"


    #############
    # HBASE MASTER
    #############

    # Port which we need to query and
    # Index information on the JSON whic has the Heap Memory information
    hbaseMaster = ["prod-master1"]
    portToQueryHbaseMaster = 60010
    indexToQueryHbaseMaster = 1

    # Dict to store all data.
    hbaseMasterListDictionary = []

    # Running through the list to create dictionary of information.
    for serverName in hbaseMaster:
        getUrl = urlFromInput(serverName, portToQueryHbaseMaster)
        if getUrl == ERROR:
            continue
        heapDictionary = gettingDataFromURL(getUrl, indexToQueryHbaseMaster)
        if heapDictionary == ERROR:
            continue
        hbaseMasterListDictionary.append(heapDictionary)

    if not hbaseMasterListDictionary == []:
        # Setting up Email Processing
        headerEmailBody = emailBodyHeader("Hbase Master")
        footerEmailBody = emailBodyFooter("Hbase Master")

        # As we have only one dictionary information we just assign it to Subject.
        for indexHbaseDictionary in hbaseMasterListDictionary:
            if not indexHbaseDictionary == {}:
                subjectEmail = emailSubjectMessageDetailed(indexHbaseDictionary['nodeStatus'],
                                           indexHbaseDictionary['usedHeapPercentage'],
                                           "HBase Master")
            else:
                subjectEmail = emailSubjectMessage("Hbase Master")

        mainMessageEmailBody = emailBodyMessageDetailed(hbaseMasterListDictionary, "GB")

        # Execute command to send all information as a mail
        print(headerEmailBody + mainMessageEmailBody + footerEmailBody + subjectEmail)
    else:
        print "ERROR : Dictionary is Empty!!"

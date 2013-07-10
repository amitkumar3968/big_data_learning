// Reducer JS 

// Getting the Container from the Mapper 
var container=li__getContainer();
var containerHelper=li__getContainerHelper();

// New get the Reducer Keys and Values from the Container.
var reduceKeys=containerHelper.getReduceKeysOfRecord();
var reduceValues=container.getReduceValues();
var reduceValuesSize=reduceValues.size();
li__debug('Executing reduce script');

// Creating Jason
var jsonData = []

for(var i=0; i < reduceValuesSize; i++)
{
	// For every Data in Container add then in each of Column, 
	// in the Array Above
	var reduceValue=containerHelper.getReduceValueOfRecord(i);
	jsonData.push(
					{
						"ipAddress":reduceValue.get(0),
						"date_s":reduceValue.get(1),
						"dateWithTime":reduceValue.get(2),
						"interfaceType":reduceValue.get(3),
						"zoneNetAddress":"10.157.0.0",
						"maxOctetsRX":reduceValue.get(4),
						"maxOctetsTX":reduceValue.get(5),
						"averageThroughputIn":reduceValue.get(6),
						"averageThroughputOut":reduceValue.get(7),
						"averageDropEvents":reduceValue.get(8),
						"averageCRCAlignError":reduceValue.get(9),
						"averageJabberPackets":reduceValue.get(10),
						"averageCollisions":reduceValue.get(11)
					}
				);
	

}

// Add Data to the Container with Updated Key Values.
containerHelper.addRecordToDataSet(reduceKeys,jsonData);

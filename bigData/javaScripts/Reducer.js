// Reducer JS 

// Getting the Container from the Mapper 
var container=li__getContainer();
var containerHelper=li__getContainerHelper();

// New get the Reducer Keys and Values from the Container.
var reduceKeys=containerHelper.getReduceKeysOfRecord();
var reduceValues=container.getReduceValues();
var reduceValuesSize=reduceValues.size();
li__debug('Executing reduce script');

// Create Array for our data
var maxOctetsRx=new Array();
var maxOctetsTx=new Array();
var averagePktsRX=new Array();
var averagePktsTX=new Array();
var averageDropEvent=new Array();
var averageCRCAlignError=new Array();
var averageJabberPackets=new Array();
var averageCollisions=new Array();
for(var i=0;i<reduceValuesSize;i++)
{
	// For every Data in Container add then in each of Column, 
	// in the Array Above
	var reduceValue=containerHelper.getReduceValueOfRecord(i);
	maxOctetsRx[i]=reduceValue.get(7);
	maxOctetsTx[i]=reduceValue.get(18);
	averagePktsRX[i]=reduceValue.get(8);
	averagePktsTX[i]=reduceValue.get(19);
	averageDropEvent[i]=reduceValue.get(6);
	averageCRCAlignError[i]=reduceValue.get(11);
	averageJabberPackets[i]=reduceValue.get(15);
	averageCollisions[i]=reduceValue.get(16);

}
li__debug('adding  new  reduced record');

// We need to Register this as this is an ArrayList
var newValues=li__getBean('newValues');

// Adding All values in the Array.
newValues.add(maxOctetsRx.max());
newValues.add(maxOctetsTx.max());
newValues.add(averagePktsRX.avg());
newValues.add(averagePktsTX.avg());
newValues.add(averageDropEvent.avg());
newValues.add(averageCRCAlignError.avg());
newValues.add(averageJabberPackets.avg());
newValues.add(averageCollisions.avg());
newValues.add(averageCRCAlignError.avg());
li__debug('Key  ' + reduceKeys);
li__debug('Values  ' );
li__debug('MaxOctetsRx ' + maxOctetsRx.max());
li__debug('MaxOctetsTx ' + maxOctetsTx.max());
li__debug('AveragePktsRX ' + averagePktsRX.avg());
li__debug('AveragePktsTX ' + averagePktsTX.avg());
li__debug('AverageDropEvent ' + averageDropEvent.avg());
li__debug('AverageCRCAlignError ' + averageCRCAlignError.avg());
li__debug('AverageJabberPackets ' + averageJabberPackets.avg());
li__debug('AverageCollisions ' + averageCRCAlignError.avg());

// Add Data to the Container with Updated Key Values.
containerHelper.addRecordToDataSet(reduceKeys,newValues);

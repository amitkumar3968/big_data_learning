
// Getting Container
var container=li__getContainer();
var containerHelper=li__getContainerHelper();
li__debug('Executing map script');

// Getting Key and Value
var mapKeyValuePairs=container.getKeyValuePairs();
var mapKeyValuePairsSize=mapKeyValuePairs.size();
li__debug(' size of records '+mapKeyValuePairsSize);

// Traversing through the KeyValue Pair to get all required Data.
// We get Date as ddmmyy:hhmm we convert it in to ddmmyy:hh (Hourly Data)

for(var i=0;i<mapKeyValuePairsSize;i++)
{
	
	li__debug(' record '+container.getKeyValuePairs());
	// Getting Keys for Each Record
	var keys=containerHelper.getKeysOfRecord(i);
	li__debug('keys of record ' + i +' '+keys);
	
	// getting Value here
	var values=containerHelper.getValuesOfRecord(i);
	li__debug('values of record ' + i +' '+values);
	li__debug('clearing keys ');
	
	// Clearing key as we will be creating a new Key for our Reducer JS
	keys.clear();
	
	// Creating ddmmyy:hh date string for our key.
	var dateformat=values.get(1);
	var pos=dateformat.indexOf(':')+3;
	dateformat=dateformat.substring(0,pos);
	
	// Creating Key Now. IPAddress, Date(ddmmyy:hh), Interface
	keys.add(values.get(0));
	keys.add(dateformat);
	keys.add(dateformat);
	keys.add(values.get(4));
	
	// Once we have the Date formated the we replace the old one,
	// with this new Date
	containerHelper.replaceColumnOfDataSet(i,1,dateformat);
	li__debug('new keys of record ' + i + ' ' + keys);
	li__debug('new values of record ' + i + ' ' + values);
	li__debug('replacing record with new vales and keys ');
	
	// Now Replacing the Key we our New Key & Value
	containerHelper.replaceRecordOfDataSet(i,keys,values);
}    

var container = li__getContainer();
var containerHelper = li__getContainerHelper();
li__debug('doing map script');
var mapKeyValuePairs = container.getKeyValuePairs();
var mapKeyValuePairsSize = mapKeyValuePairs.size();
li__debug(' record ' + container.getKeyValuePairs());
li__debug(' size ' + mapKeyValuePairsSize);
for (var i = 0; i < mapKeyValuePairsSize; i++) {
    var keys = containerHelper.getKeysOfRecord(i);
    li__debug('keys ' + keys);
    var values = containerHelper.getValuesOfRecord(i);
    li__debug('values ' + values);
    li__debug('clearing keys ');
    keys.clear();
    li__debug('keys ' + keys);
    li__debug('value ' + values.get(0));
    keys.add(values.get(0));
    li__debug('new keys ' + keys);
    li__debug('replacing new record');
    containerHelper.replaceRecordOfDataSet(i, keys, values);
}

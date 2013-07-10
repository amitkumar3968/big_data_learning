var container = li__getContainer();
var containerHelper = li__getContainerHelper();
var reduceKeys = containerHelper.getReduceKeysOfRecord();
var reduceValues = container.getReduceValues();
var reduceValuesSize = reduceValues.size();
var sum1 = 0;
var sum2 = 0;
for (var i = 0; i < reduceValuesSize; i++) {
    var reduceValue = containerHelper.getReduceValueOfRecord(i);
    sum1 += parseInt(reduceValue.get(1));
    sum2 += parseInt(reduceValue.get(2));
}
li__debug('adding  new  reduced record');
var newValues = li__getBean('newValues');
newValues.add(sum1);
newValues.add(sum2);
containerHelper.addRecordToDataSet(reduceKeys, newValues);

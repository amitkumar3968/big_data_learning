def backupMysql():
    print 'Call'
    pass

array = []
stringInfo = 'this iS a String &^ 123 and I need to remove any of the string is in'
for item in stringInfo:
    item.lower()
    #print ord(item)
    if ord(item) >= ord('a') and ord(item) <= ord('z'):
        info = ord(item) - ord('a')
        array.insert(info,array.index(info) + 1)
        if array.__len__() > 2:
            array.pop(info+1)
print array


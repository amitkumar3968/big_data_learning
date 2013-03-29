import csv
import MySQLdb

mydb = MySQLdb.connect(host='192.168.157.131',user='root', passwd='', db='tellabs_csv_data')
cursor = mydb.cursor()

print cursor

csv_data = csv.reader(file('students.csv'))
csv_data.next()
for row in csv_data:
    row_update = []
    row_update.append(row[0])
    row_update.append(row[1])
    intval = int(row[2])
    row_update.append(intval)
    print row_update
    cursor.execute('INSERT INTO test_csv(name, class, mark ) VALUES("%s", "%s", "%d")', row_update)
#close the connection to the database.
mydb.commit()

cursor.close()
print "Done"

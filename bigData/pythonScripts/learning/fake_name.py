import csv

"""
file_name = "fake_names.csv"
csv_info = csv.DictReader(open(file_name, "rb"),delimiter=",",quotechar='"')

for info in csv_info:
    if info['City'] == "Abbeville":
        print info['GivenName']
        print info
"""

class data_reader(object):
    dictionary = []
    def __init__(self, file_name_path, delimiter, quotechar):
        self.file_name_path = file_name_path
        self.delimiter = delimiter
        self.quotechar = quotechar

    def create_dictionary(self):
        self.dictionary = csv.DictReader(open(self.file_name_path, "rb"), delimiter=self.delimiter)

    def print_data_for_key(self, key):
        if key.isalpha() == True:
            for item in self.dictionary:
                print item[key]

    def print_name_for_key_value(self, key, value):
        if key.isalpha() == True:
            for item in self.dictionary:
                if item[key] == value:
                    print item['GivenName'], item['Surname'], "\n\t|\n\t-Contact Number:", item['TelephoneNumber']

    """
    def get_data_by_occupation(occupation):
    def get_data_by_location(location):
    def get_data_by_key(key):
    """
    def get_data_by_doy(self, doy):
        if isinstance(doy, int) == True:
            for item in self.dictionary:
                if item['Birthday'][-4::] == str(doy) and item['Occupation'].find('911') != -1:
                    print item['Birthday'][-4::], item['Occupation'], item['GivenName'], item['Surname']

    def get_data_by_occupation(self, occupation):
        count = 0
        if isinstance(occupation, str) == True:
            for item in self.dictionary:
                if item['Occupation'].find(occupation) != -1:
                    print item['Birthday'][-4::], "\n\t|\n\t-",item['Occupation'], "\n\t|\n\t-", item['GivenName'], item['Surname']
                    count = count + 1
            print "Total People Related to Occupation \"%s\": %d" %(occupation, count)




data_to_get = data_reader("fake_names.csv", ",", '"')
data_to_get.create_dictionary()
data_to_get.get_data_by_occupation("Civil engineering")




#data_to_get.print_data_for_key("City")
#data_to_get.print_name_for_key_value("City","Santa Clara")



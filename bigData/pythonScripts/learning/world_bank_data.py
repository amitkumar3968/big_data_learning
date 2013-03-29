import csv
import re
import locale

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

    def print_countries(self):
        info_list = []
        unique_list = []
        for items in self.dictionary:
            info_list.append(items['Borrower Country'])

        unique_list = list(set(info_list))
        # Now lets Print this new Unique list
        # for info in unique_list:
        #    print info

        return unique_list

    def int_million_system(self, number):
        string_num = str(number)
        group_str = []
        new_string = ""
        while string_num and string_num[-1].isdigit():
            group_str.append(string_num[-3:])
            string_num = string_num[:-3]
        new_string = string_num + ",".join(reversed(group_str))
        return new_string



    def print_companies(self, signing_month):
        total_money = 0
        if isinstance(signing_month, str) == True:
            for item in self.dictionary:
                """
                re.split(' ',item['Contract Signing Date']) ==> ['1/12/2012', '12:00:02', 'AM']
                re.split('/', re.split(' ',item['Contract Signing Date'])[0]) ==> ['1', '12', '2012']
                re.split('/', re.split(' ',item['Contract Signing Date'])[0])[0] ==> '1'
                """
                info = re.split('/', re.split(' ',item['Contract Signing Date'])[0])[0]
                if info == signing_month:
                    print item['Borrower Country'], item['Contract Signing Date'], item['Total Contract Amount (USD)']
                    total_money = total_money + int(item['Total Contract Amount (USD)'][1:-3:])

        print "Total Amount during the Month "+ signing_month +": $" + self.int_million_system(total_money) + ".00"


world_bank_data = data_reader("world_bank_contracts.csv",",",'"')
world_bank_data.create_dictionary()
#world_bank_data.print_countries()
month_input = raw_input("Enter the Month to get data from 01 to 12: ")
world_bank_data.print_companies(month_input)


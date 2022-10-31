import random

mib_dictionary = {}
f = open("file_to_analyize.yaml", "r")


class line_item:
    def __init__(self, mib, oid):
        self.mib = mib
        self.oid = oid

def scan_mib_file(file_to_analyize):
    i = 0
    for row in file_to_analyize:
        i += 1
        split_key_value = row.split(':')
        mib_name = split_key_value[0]
        oid = split_key_value[1].strip("\n")
        row = line_item(mib_name, oid)
        mib_dictionary[row.mib] = row.oid


scan_mib_file(f)

def create_snmp_rec(dict_to_scan):
    data_type = [2,4,5,6,64,65,66,67,68,70]
    
    for row in dict_to_scan:
        metric_value = random.randint(1,22)
        string_value = random.choice(['Cisco', 'Juniper', 'Sophos'])
        other_string_value = random.choice(['UP', 'DOWN', 'OK'])
        if row.endswith(str(1)) == True : 
            scalar_obj = str(row) + "|" + str(data_type[0]) + "|" + str(metric_value)
            print(scalar_obj)
        elif row.endswith(str(2)) == True:
            tabular_obj = str(row) + "|" + str(data_type[1]) + "|" + str(metric_value)
            print(tabular_obj)
        elif row.endswith(str(3)) == True:
            tabular_obj = str(row) + "|" + str(data_type[1]) + "|" + str(string_value)
            print(tabular_obj)
        else:
            tabular_obj = str(row) + "|" + str(data_type[1]) + "|" + str(other_string_value)
            print(tabular_obj)


create_snmp_rec(mib_dictionary.values())




#Program to emulate a DNS server
#By : Omkar Shinde

#dns1.txt is the file which stores the records.
#Every time a search is performed the entries are pulled from this file.

import re
record = []
temp = ''
f = open('dns1.txt', 'r')
for line in f:
    temp = line
    string = temp[1:-3].split(',')
    temp = ''
    record.append(string)

while 1:
    option = input('\n\nEnter Option :\n1 : Search 2: Add 3: View Records 4: Delete Entry 5: Exit\n')
    
    # 1 SEARCH
    if option == 1:
        stype = input("Search by\n1: Domain name 2: IP\n");
        if stype == 1:
            search = input('Enter domain name : ')
            for sublist in record:
                if sublist[0] == search:
                    print "\nAddress found: "
                    print search+" -> "+sublist[4]
        if stype == 2:
            search = input('Enter IP address : ')
            for sublist in record:
                if sublist[4] == search:
                    print "\nAddress found: "
                    print search+" -> "+sublist[0]
        
    # 2 ADD ENTRY
    if option == 2:
        entry = []
        domain_name = input('Enter the domain name : ')
        entry.append(domain_name)
        time_to_live = input('Enter the Time to live : ')
        entry.append(time_to_live)
        entry_class = input('Enter class (default IN) : ')
        entry.append(entry_class)
        entry_type = input('Enter type : ')
        entry.append(entry_type)
        entry_value = input('Enter value : ')
        entry.append(entry_value)
        record.append(entry)

        # Add record to file
        f = open('dns1.txt', 'a')
        w = '['+','.join(entry)+']\n'
        f.write(w)
        f.close()
        
    # 3 VIEW RECORDS    
    if option == 3:
        for entry in record:
                print entry
    # 4 DELETE
    if option == 4:
        searchs = input('Enter domain name entry to delete: ')
        file = open('dns1.txt')
        lines = file.readlines()
        file.close()
        for i, line in enumerate(lines):
            if searchs.search(line):
                print i, line
                
    # 5 BREAK
    if option == 5:
        break
print 'Exit'

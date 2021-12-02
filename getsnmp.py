import os

def search(file_name, search_string):
    """Search for the given string in file and return lines contaning that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r',encoding="utf-8",errors="ignore") as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            line_number +=1
            # For each line, check if line contains the string
            if search_string in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results


def search_multiple(file_name, list_of_strings):
    """Get line from the file along with line numbers, which contains any string from the list"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode use encoding and erros to block the error String
    with open(file_name, 'r',encoding="utf-8",errors="ignore") as read:
        # Read all lines in the file one by one
        for line in read:
            line_number += 1
            # For each line, check if line contains any string from the list of strings
            for x in list_of_strings:
                #Filter unwanted value
                if x in line.rstrip():
                    # If any string is found in line, then append that line along with line number in list
                    list_of_results.append((x,line_number,line.rstrip()))

    # Return list of tuples containing matched string, line numbers and lines where string is found
    return list_of_results

def main():

    #If foler exists , delete the foler
    filepath="C:\mib_information\SNMPINFO\pythonsnmp.txt"
    if os.path.exists(filepath):
        os.remove(filepath)

    #Input snmp file name
    dir = 'C:\mib_information\SNMPINFO'
    format = 'txt'
    count = 100
    for a in range(count):
        count -= 1
        print("Please enter the file you want to analyze  ex:snmpinfo :")
        snmp = input()

        # combain the folder
        folder = os.path.join(dir, snmp + '.' + format)
        if os.path.isfile(folder):
            break
    #----------------------------------------------------------------------

    #Input nic card model and total ports
    nicmodel,nicports = input("Please input your nic model and nic ports ex:361T 2 or 369i 4  :").split()

    matched_lines = search(folder, nicmodel)

    #Create the discriminant and gernerate the data in the txt file

    if nicports == "2" :
        for line in matched_lines:
            if "0000" in line:
                continue
            print(line)

            #Generate txt file to save data
            with open("pythonsnmp.txt", "w") as file:
                for line in matched_lines:
                    if "0000" in line:
                        continue
                    print(line, file=file, sep='\n')

    if nicports == "4" :
        for line in matched_lines:
            if "0000" in line:
                continue
            print (line)

            #Generate txt file to save data
            with open("pythonsnmp.txt", "w") as file:
                for line in matched_lines:
                    if "0000" in line:
                        continue
                    print(line, file=file, sep='\n')
# ----------------------------------------------------------------------
    #Grab the discards and errors data
    if nicports == "2" :
        verify1,verify2 = input("Please input " +nicports+ " number to verify error and discards ex:1 2  :").split()
        matched_lines = search_multiple(folder,
                                        ['[interfaces.ifTable.ifEntry.ifInDiscards.' + verify1 + ']' ,'[interfaces.ifTable.ifEntry.ifInDiscards.' + verify2 + ']' ,'[interfaces.ifTable.ifEntry.ifInErrors.' + verify1 + ']' ,'[interfaces.ifTable.ifEntry.ifInErrors.' + verify2 + ']'])



        for x in matched_lines:
                print('Line = ', x[2])

    elif nicports == "4":
        verify1 , verify2 , verify3 , verify4 = input("Please input  " +nicports+ " number to verify error and discards:  ex:1 2 3 4  :").split()
        matched_lines = search_multiple(folder,['[interfaces.ifTable.ifEntry.ifInDiscards.' + verify1 + ']','[interfaces.ifTable.ifEntry.ifInDiscards.' + verify2 + ']','[interfaces.ifTable.ifEntry.ifInDiscards.' + verify3 + ']','[interfaces.ifTable.ifEntry.ifInDiscards.' + verify4 + ']','[interfaces.ifTable.ifEntry.ifInErrors.' + verify1 + ']', '[interfaces.ifTable.ifEntry.ifInErrors.' + verify2+ ']', '[interfaces.ifTable.ifEntry.ifInErrors.' + verify3+ ']', '[interfaces.ifTable.ifEntry.ifInErrors.' + verify4+ ']'])

        for x in matched_lines:
                print('Line = ', x[2])

    # Reopen txt and create the data in the txt file
    file = open("pythonsnmp.txt", "a")
    for x in matched_lines:
        if x in matched_lines:
            file.write(x[2] + '\n')

    # ----------------------------------------------------------------------

    #Pause the system
    os.system("pause")

#Execute main()
if __name__ == '__main__':
    main()


import sys
import os
import tkinter as tk
import tkinter.font as tkFont




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
                #list_of_results.append((line_number,line.rstrip()))
                list_of_results.append((line.rstrip()))

    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results


def search_multiple(file_name, list_of_strings):
    """Get the line and line number from the file, which contains any string in the list """
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
                if x in line:
                    # If any string is found in line, then append that line along with line number in list
                    list_of_results.append((x,line_number,line.rstrip()))
    # Return list of tuples containing matched string, line numbers and lines where string is found
    return list_of_results

def nic_port():
    dir = 'C:\mib_information\SNMPINFO'
    format = 'txt'
    snmp = (snmp_entry.get())
    folder = os.path.join (dir ,snmp+'.'+format )
    nic = (nic_entry.get())
    nicports = (nicport_entry.get())
    nicmodel = search(folder, nic)
    if nicports == "2":
        for line in nicmodel:
            if "0000" in line:
                continue
            result_label.configure(text=result_label.cget('text') + str(line) + '\n',wraplength=1000,font=fontExample2)



    if nicports == "4":
        for line in nicmodel:
            if "0000" in line:
                continue
            result_label.configure(text=result_label.cget('text') + str(line) + '\n',wraplength=1000,font=fontExample2)



def verify_port():
    dir = 'C:\mib_information\SNMPINFO'
    format = 'txt'
    snmp = (snmp_entry.get())
    folder = os.path.join (dir ,snmp+'.'+ format )
    nicports = (nicport_entry.get())
    if nicports == "2":
        verifynumber = (verifynumber_entry.get())
        verify1,verify2 = verifynumber.split()
        matched_lines = search_multiple(folder,
                                        ['[interfaces.ifTable.ifEntry.ifInDiscards.' + verify1 + ']' ,'[interfaces.ifTable.ifEntry.ifInDiscards.' + verify2 + ']' ,'[interfaces.ifTable.ifEntry.ifInErrors.' + verify1 + ']' ,'[interfaces.ifTable.ifEntry.ifInErrors.' + verify2 + ']'])


        for x in matched_lines:
            #Create output in the tkinter
            result2_label.configure(text=result2_label.cget('text') + str(x[2]) + '\n',wraplength=700,font=fontExample2)

    if nicports == "4":
        verifynumber = (verifynumber_entry.get())
        verify1,verify2,verify3,verify4 = verifynumber.split()
        matched_lines = search_multiple(folder,['[interfaces.ifTable.ifEntry.ifInDiscards.' + verify1 + ']','[interfaces.ifTable.ifEntry.ifInDiscards.' + verify2 + ']','[interfaces.ifTable.ifEntry.ifInDiscards.' + verify3 + ']','[interfaces.ifTable.ifEntry.ifInDiscards.' + verify4 + ']','[interfaces.ifTable.ifEntry.ifInErrors.' + verify1 + ']', '[interfaces.ifTable.ifEntry.ifInErrors.' + verify2+ ']', '[interfaces.ifTable.ifEntry.ifInErrors.' + verify3+ ']', '[interfaces.ifTable.ifEntry.ifInErrors.' + verify4+ ']'])
        for x in matched_lines:
            #Create output in the tkinter
            result2_label.configure(text=result2_label.cget('text') + str(x[2]) + '\n',wraplength=700,font=fontExample2)

#Tkinter clear function
def clear():
    result_label.configure(text="") , result2_label.configure(text="")

#Save the nec image on tkinter
def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return f'{os.path.join(sys._MEIPASS, filename)}'
    else:
        return f'{filename}'

#Create title
window = tk.Tk()
window.title('NEC Taiwan Server R&D Center ')
window.geometry('1200x850')
window.iconbitmap(get_path("NEC.ico"))


#Create the Font selection
fontExample = tkFont.Font(family="Segoe UI", size=20)
fontExample2 = tkFont.Font(family="Segoe UI", size=10)
fontExample3 = tkFont.Font(family="Segoe UI", size=15)
header_label = tk.Label(window, text='IO Device Team',font=fontExample)
header_label.pack()

#Create the TXT name row
snmp_frame = tk.Frame(window)
snmp_frame.pack(side=tk.TOP)
snmp_label = tk.Label(snmp_frame, text='TXT name:',font=fontExample2,padx=5,pady=10)
snmp_label.pack(side=tk.LEFT)
snmp_entry = tk.Entry(snmp_frame)
snmp_entry.pack(side=tk.LEFT)

nic_frame = tk.Frame(window)
nic_frame.pack(side=tk.TOP)
nic_label = tk.Label(nic_frame, text='NIC model:',font=fontExample2,padx=5,pady=10)
nic_label.pack(side=tk.LEFT)
nic_entry = tk.Entry(nic_frame)
nic_entry.pack(side=tk.LEFT)

nicport_frame = tk.Frame(window)
nicport_frame.pack(side=tk.TOP)
nicport_label = tk.Label(nicport_frame, text='NIC ports:',font=fontExample2,padx=5,pady=10)
nicport_label.pack(side=tk.LEFT)
nicport_entry = tk.Entry(nicport_frame)
nicport_entry.pack(side=tk.LEFT)

#Create result output
result_label = tk.Label(window)
result_label.pack()

calculate_btn = tk.Button(window, text='First analysis', command=nic_port,font=fontExample3,padx=5,pady=10)
calculate_btn.pack()

verifynumber_frame = tk.Frame(window)
verifynumber_frame.pack(side=tk.TOP,padx=5,pady=10)
verifynumber_label = tk.Label(verifynumber_frame, text='NIC numbers:',font=fontExample2)
verifynumber_label.pack(side=tk.LEFT,padx=5,pady=10)
verifynumber_entry = tk.Entry(verifynumber_frame)
verifynumber_entry.pack(padx=5,pady=10)

#Create result2 output
result2_label = tk.Label(window)
result2_label.pack()


calculate_btn = tk.Button(window, text='Second analysis', command=verify_port,font=fontExample3,padx=5,pady=10)
calculate_btn.pack()


clear_label = tk.Label(window)
clear_label.pack()
clear_btn= tk.Button(window,text="Clear", command=clear,font=fontExample3,padx=5,pady=10)
clear_btn.pack()

window.mainloop()


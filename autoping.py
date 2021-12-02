import sys
import os
import tkinter as tk
import tkinter.font as tkFont

#Save the nec image on tkinter
def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return f'{os.path.join(sys._MEIPASS, filename)}'
    else:
        return f'{filename}'

def ping_2c():
    #host = ["192.168.10.1","192.168.10.11","192.168.20.2","192.168.20.22"]
    host = ["192.168.10.11","192.168.20.22"]
    for ip in host:
        response = os.system("ping -n 1 " + ip + ">null")
        if response == 0:
            result_label.configure(text=result_label.cget('text')+(ip + " connection") + '\n', wraplength=700,font=fontExample3)
        else:
            result_label.configure(text=result_label.cget('text') +(ip + " disconnection") + '\n', wraplength=700,font=fontExample3)

def ping_2s():
    #host = ["192.168.10.1","192.168.10.11","192.168.20.2","192.168.20.22"]
    host = ["192.168.10.1","192.168.20.2"]
    for ip in host:
        response = os.system("ping -n 1 " + ip + ">null")
        if response == 0:
            result_label.configure(text=result_label.cget('text')+(ip + " connection") + '\n', wraplength=700,font=fontExample3)
        else:
            result_label.configure(text=result_label.cget('text') +(ip + " disconnection") + '\n', wraplength=700,font=fontExample3)

def ping_4c():
    #host = ["192.168.10.1","192.168.10.11","192.168.20.2","192.168.20.22","192.168.30.3","192.168.30.33","192.168.40.4","192.168.40.44"]
    host = ["192.168.10.11","192.168.20.22","192.168.30.33","192.168.40.44"]
    for ip in host:
        response = os.system("ping -n 1 " + ip + ">null")
        if response == 0:
            result_label.configure(text=result_label.cget('text') + (ip + " connection") + '\n', wraplength=700,font=fontExample3)
        else:
            result_label.configure(text=result_label.cget('text') + (ip + " disconnection") + '\n', wraplength=700,font=fontExample3)

def ping_4s():
    #host = ["192.168.10.1","192.168.10.11","192.168.20.2","192.168.20.22","192.168.30.3","192.168.30.33","192.168.40.4","192.168.40.44"]
    host = ["192.168.10.1","192.168.20.2","192.168.30.3","192.168.40.4"]
    for ip in host:
        response = os.system("ping -n 1 " + ip + ">null")
        if response == 0:
            result_label.configure(text=result_label.cget('text') + (ip + " connection") + '\n', wraplength=700,font=fontExample3)
        else:
            result_label.configure(text=result_label.cget('text') + (ip + " disconnection") + '\n', wraplength=700,font=fontExample3)

def clear():
    result_label.configure(text="")

window = tk.Tk()
window.title('NEC Taiwan Server R&D Center ')
window.geometry('1000x800')
window.iconbitmap(get_path("NEC.ico"))

fontExample = tkFont.Font(family="Segoe UI", size=20)
fontExample3 = tkFont.Font(family="Segoe UI", size=15)
header_label = tk.Label(window, text='IO Device Team',font=fontExample)
header_label.pack()


calculate_btn = tk.Button(window, text='Ping 2 Clients', command=ping_2c,font=fontExample3,padx=5,pady=10)
calculate_btn.pack(side = 'left')
calculate_btn.pack(padx=10)

calculate3_btn = tk.Button(window, text='Ping 2 Servers', command=ping_2s,font=fontExample3,padx=5,pady=10)
calculate3_btn.pack(side = 'left')
calculate3_btn.pack(padx=10)

calculate2_btn = tk.Button(window, text='Ping 4 Clients', command=ping_4c, font=fontExample3, padx=5, pady=10)
calculate2_btn.pack(side = 'left')
calculate2_btn.pack(padx=10)


calculate4_btn = tk.Button(window, text='Ping 4 Servers', command=ping_4s, font=fontExample3, padx=5, pady=10)
calculate4_btn.pack(side = 'left')
calculate4_btn.pack(padx=10)


result_label = tk.Label(window)
result_label.pack(pady=100)



clear_label = tk.Label(window)
clear_label.pack()
clear_btn= tk.Button(window,text="Clear", command=clear,font=fontExample,padx=5,pady=10)
clear_btn.pack(side = 'bottom')
clear_btn.pack(pady = 50)

window.mainloop()

import filecmp
import tkinter as tk
import tkinter.font as tkFont
import sys


def clear():
    result_label.configure(text="")

def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return f'{os.path.join(sys._MEIPASS, filename)}'
    else:
        return f'{filename}'


def disk_verify():
    disk = (number_entry.get())

    if disk == "1" :
        # disk1
        DIRS = [r'E:\Newtest\1', r'E:\Newtest\2', r'E:\Newtest\3', r'E:\Newtest\4', r'E:\Newtest\5', r'E:\Newtest\6',
                r'E:\Newtest\7', r'E:\Newtest\8', r'E:\Newtest\9', r'E:\Newtest\10']
        FILES = [('copy1.txt', 'copy2.txt'), ('fcmp1.txt', 'fcmp2.txt'), ('filecp1.txt', 'filecp2.txt')]

        for e, dir in enumerate(DIRS, 1):
            cmp = True
            for file in FILES:
                try:
                    if not filecmp.cmp(os.path.join(dir, file[0]), os.path.join(dir, file[1])):
                        cmp = False
                        break
                except Exception as ex:
                    print(f'Error -> {ex}', file=sys.stderr)
                    continue
            # print(f'E_{e} compare {"pass" if cmp else "fail"}')
            x = (f'E_{e} compare {"pass" if cmp else "fail"}')
            result_label.configure(text=result_label.cget('text') + x + '\n')


    #For two dis2
    if disk == "2" :

        #disk1
        DIRS = [r'E:\Newtest\1', r'E:\Newtest\2', r'E:\Newtest\3',r'E:\Newtest\4',r'E:\Newtest\5',r'E:\Newtest\6',r'E:\Newtest\7',r'E:\Newtest\8',r'E:\Newtest\9',r'E:\Newtest\10']
        FILES = [('copy1.txt', 'copy2.txt'), ('fcmp1.txt', 'fcmp2.txt'), ('filecp1.txt', 'filecp2.txt')]

        for e, dir in enumerate(DIRS, 1):
            cmp = True
            for file in FILES:
                try:
                    if not filecmp.cmp(os.path.join(dir, file[0]), os.path.join(dir, file[1])):
                        cmp = False
                        break
                except Exception as ex:
                        print(f'Error -> {ex}', file=sys.stderr)
                        continue
            #print(f'E_{e} compare {"pass" if cmp else "fail"}')
            x = (f'E_{e} compare {"pass" if cmp else "fail"}')
            result_label.configure(text=result_label.cget('text') + x + '\n')

        #disk2
        DIRS = [r'F:\Newtest\1', r'F:\Newtest\2', r'F:\Newtest\3',r'F:\Newtest\4',r'F:\Newtest\5',r'F:\Newtest\6',r'F:\Newtest\7',r'F:\Newtest\8',r'F:\Newtest\9',r'F:\Newtest\10']
        FILES = [('copy1.txt', 'copy2.txt'), ('fcmp1.txt', 'fcmp2.txt'), ('filecp1.txt', 'filecp2.txt')]

        for e, dir in enumerate(DIRS, 1):
            cmp = True
            for file in FILES:
                try:
                    if not filecmp.cmp(os.path.join(dir, file[0]), os.path.join(dir, file[1])):
                        cmp = False
                        break
                except Exception as ex:
                    print(f'Error -> {ex}', file=sys.stderr)
                    continue
            #print(f'F_{e} compare {"pass" if cmp else "fail"}')
            x = (f'F_{e} compare {"pass" if cmp else "fail"}')
            result_label.configure(text=result_label.cget('text') + x + '\n')



#For 4 disks
    if disk == "4":

        #disk1
        DIRS = [r'E:\Newtest\1', r'E:\Newtest\2', r'E:\Newtest\3',r'E:\Newtest\4',r'E:\Newtest\5',r'E:\Newtest\6',r'E:\Newtest\7',r'E:\Newtest\8',r'E:\Newtest\9',r'E:\Newtest\10']
        FILES = [('copy1.txt', 'copy2.txt'), ('fcmp1.txt', 'fcmp2.txt'), ('filecp1.txt', 'filecp2.txt')]

        for e, dir in enumerate(DIRS, 1):
            cmp = True
            for file in FILES:
                try:
                    if not filecmp.cmp(os.path.join(dir, file[0]), os.path.join(dir, file[1])):
                        cmp = False
                        break
                except Exception as ex:
                    print(f'Error -> {ex}', file=sys.stderr)
                    continue
            x = (f'E_{e} compare {"pass" if cmp else "fail"}')
            result_label.configure(text=result_label.cget('text') + x + '\n')

        #disk2
        DIRS = [r'F:\Newtest\1', r'F:\Newtest\2', r'F:\Newtest\3', r'F:\Newtest\4', r'F:\Newtest\5', r'F:\Newtest\6',
                r'F:\Newtest\7', r'F:\Newtest\8', r'F:\Newtest\9', r'F:\Newtest\10']
        FILES = [('copy1.txt', 'copy2.txt'), ('fcmp1.txt', 'fcmp2.txt'), ('filecp1.txt', 'filecp2.txt')]

        for e, dir in enumerate(DIRS, 1):
            cmp = True
            for file in FILES:
                try:
                    if not filecmp.cmp(os.path.join(dir, file[0]), os.path.join(dir, file[1])):
                        cmp = False
                        break
                except Exception as ex:
                    print(f'Error -> {ex}', file=sys.stderr)
                    continue
            x = (f'F_{e} compare {"pass" if cmp else "fail"}')
            result_label.configure(text=result_label.cget('text') + x + '\n')

        #disk3
        DIRS = [r'G:\Newtest\1', r'G:\Newtest\2', r'G:\Newtest\3', r'G:\Newtest\4', r'G:\Newtest\5', r'G:\Newtest\6',
                r'G:\Newtest\7', r'G:\Newtest\8', r'G:\Newtest\9', r'G:\Newtest\10']
        FILES = [('copy1.txt', 'copy2.txt'), ('fcmp1.txt', 'fcmp2.txt'), ('filecp1.txt', 'filecp2.txt')]

        for e, dir in enumerate(DIRS, 1):
            cmp = True
            for file in FILES:
                try:
                    if not filecmp.cmp(os.path.join(dir, file[0]), os.path.join(dir, file[1])):
                        cmp = False
                        break
                except Exception as ex:
                    print(f'Error -> {ex}', file=sys.stderr)
                    continue
            x = (f'G_{e} compare {"pass" if cmp else "fail"}')
            result_label.configure(text=result_label.cget('text') + x + '\n')

        #disk4
        DIRS = [r'H:\Newtest\1', r'H:\Newtest\2', r'H:\Newtest\3', r'H:\Newtest\4', r'H:\Newtest\5', r'H:\Newtest\6',
                r'H:\Newtest\7', r'H:\Newtest\8', r'H:\Newtest\9', r'H:\Newtest\10']
        FILES = [('copy1.txt', 'copy2.txt'), ('fcmp1.txt', 'fcmp2.txt'), ('filecp1.txt', 'filecp2.txt')]

        for e, dir in enumerate(DIRS, 1):
            cmp = True
            for file in FILES:
                try:
                    if not filecmp.cmp(os.path.join(dir, file[0]), os.path.join(dir, file[1])):
                        cmp = False
                        break
                except Exception as ex:
                    print(f'Error -> {ex}', file=sys.stderr)
                    continue
            x = (f'H_{e} compare {"pass" if cmp else "fail"}')
            result_label.configure(text=result_label.cget('text') + x + '\n')



window = tk.Tk()
window.title('NEC Taiwan Server R&D Center ')
window.geometry('1400x820')
window.iconbitmap(get_path("NEC.ico"))



fontExample = tkFont.Font(family="Segoe UI", size=20)
fontExample2 = tkFont.Font(family="Segoe UI", size=10)
fontExample3 = tkFont.Font(family="Segoe UI", size=15)
header_label = tk.Label(window, text='IO Device Team',font=fontExample)
header_label.pack()

number_frame = tk.Frame(window)
number_frame.pack(side=tk.TOP)
number_label = tk.Label(number_frame, text='Number of disks',font=fontExample2)
number_label.pack(side=tk.LEFT)
number_entry = tk.Entry(number_frame)
number_entry.pack(side=tk.LEFT)
result_label = tk.Label(window ,wraplength=600 )
result_label.pack()
calculate_btn = tk.Button(window, text='Compare files', command=disk_verify,font=fontExample3)
calculate_btn.pack()


clear_label = tk.Label(window)
clear_label.pack()
clear_btn= tk.Button(window,text="Clear", command=clear,font=fontExample3)
clear_btn.pack()

window.mainloop()


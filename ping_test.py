import sys
import os
import subprocess

ping = input("Please input what type you want to ping. (2c=2client ,4s=4server) :")

if ping == "2c":
    host = ["192.168.10.11","192.168.20.22"]
    for ip in host:
        response = subprocess.call("ping -n 1 " + ip )
        if response == 0:
            print ("**" + ip + " ping pass")

        elif response == 2:
            print ("**" + ip + "no respone ")

        else:
            print ("**"ip + " ping fail")


if ping == "2s":
    host = ["192.168.10.1","192.168.20.2"]
    for ip in host:
        response = subprocess.call("ping -n 1 " + ip )
        if response == 0:
            print ("**" + ip + " ping pass")

        elif response == 2:
            print ("**" + ip + "no respone ")

        else:
            print ("**"ip + " ping fail")


if ping == "4c":
    host = ["192.168.10.11","192.168.20.22","192.168.30.33","192.168.40.44"]
    for ip in host:
        response = subprocess.call("ping -n 1 " + ip )
        if response == 0:
            print ("**" + ip + " ping pass")

        elif response == 2:
            print ("**" + ip + "no respone ")

        else:
            print ("**"ip + " ping fail")


if ping == "4s":
    host = ["192.168.10.1","192.168.20.2","192.168.30.3","192.168.40.4"]
    for ip in host:
        response = subprocess.call("ping -n 1 " + ip )
        if response == 0:
            print ("**" + ip + " ping pass")

        elif response == 2:
            print ("**" + ip + "no respone ")

        else:
            print ("**"ip + " ping fail")


os.system("pause")

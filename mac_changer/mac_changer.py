import subprocess

interface = input("interface > ")
new_mac = input("new mac > ")

subprocess.run("ifconfig "+ interface + " down ", shell=True)
subprocess.run("ifconfig "+ interface + " hw ether " + new_mac, shell=True)
subprocess.run("ifconfig "+ interface + " up ", shell=True)
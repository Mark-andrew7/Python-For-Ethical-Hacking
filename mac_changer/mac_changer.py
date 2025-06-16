import subprocess

interface = "wlan0"
new_mac = "00:11:22:33:44:55"

subprocess.run("ifconfig "+ interface + " down ", shell=True)
subprocess.run("ifconfig "+ interface + " hw ether " + new_mac, shell=True)
subprocess.run("ifconfig "+ interface + " up ", shell=True)

import re
import subprocess
import time

output = "cat /sys/bus/w1/devices/28-01889300007d/w1_slave"


def read_file(filename):
    doc = open(filename,'r')
    lines = doc.readlines()
    for line in lines:
        print(line)

try:
    while True:
        if time.time() >= prevtime +2:
            output = subprocess.check_output("cat /sys/bus/w1/devices/28-01889300007d/w1_slave", shell=True)
            output = re.sub('.*t=','',str(output))
            output = re.sub("[']",'',str(output))
            print(f'de temperatuur is {output}')



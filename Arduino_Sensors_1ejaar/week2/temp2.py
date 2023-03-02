import time
prevtime = time.time()
document = '/sys/bus/w1/devices/28-01889300007d/w1_slave'

def read_file(filename):
    doc = open(filename,'r')
    lines = doc.readlines()
    line = lines[1]
    line = line.split('t=')
    line = line[1].split('\n')
    print(f'De temperatuur is {float(line[0])/1000} graden Celsius')
    doc.close()

try:
    while True:
        if time.time() >= prevtime +2:
            read_file(document)
            prevtime= time.time()
except KeyboardInterrupt as e:
    print(e)

    

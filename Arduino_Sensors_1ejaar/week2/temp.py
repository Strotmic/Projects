import matplotlib
matplotlib.use('Pdf')
import matplotlib.pyplot as plt
from RPi import GPIO
moto = 21
prev_temp = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(moto, GPIO.OUT)

m_pwm = GPIO.PWM(moto,50)

document = '/sys/bus/w1/devices/28-01889300007d/w1_slave'
temperaturen=[]

def plot_grafiek():
    plt.plot(temperaturen)
    plt.ylabel('temperatuur')
    plt.savefig('/home/pi/Documents/python/pdf/test.pdf')

def read_file(filename):
    doc = open(filename,'r')
    lines = doc.readlines()
    line = lines[1]
    line = line.split('t=')
    line = line[1].rstrip('\n')
    print(f'De temperatuur is {float(line)/1000} \u00b0Celsius')
    doc.close()
    return float(line)/1000

def vent(temp, temp_set):
    m_pwm.start(0)
    if temp<temp_set:
        m_pwm.stop()
    if temp>=temp_set and temp+2<temp_set:
        m_pwm.ChangeDutyCycle(50)
    if temp+2>temp_set:
        m_pwm.ChangeDutyCycle(70)

try:
    gewenst = float(input('Geef de gewenste temperatuur op: '))
    prev_temp = read_file(document)
    while True:
        temp = read_file(document)
        temperaturen.append(temp)
        if prev_temp + 0.5<temp or prev_temp-0.5>temp:
            vent(temp, gewenst)
            prev_temp = temp
        
        if(len(temperaturen)%10==0):
            plot_grafiek()

except KeyboardInterrupt as e:
    print(e)

finally:
    print("Script has stopped!")
    GPIO.cleanup()
from RPi import GPIO

GPIO.setmode(GPIO.BCM)

vent = 21
GPIO.setup(vent, GPIO.OUT) 
pwm_vent = GPIO.PWM(vent, 50)

prev_temp = 0

temp_set = float(input('Geef een set temperatuur op'))

def read_file(filename):
    doc = open(filename,'r')
    lines = doc.readlines()
    line = lines[1]
    line = line.split('t=')
    line = line[1].rstrip('\n')
    print(f'De temperatuur is {float(line)/1000} graden Celsius')
    doc.close()
    return(float(line)/1000)

def vent_set(temp,temp_set):
    pwm_vent.start(0)
    if temp<temp_set:
        pwm_vent.stop()
    elif temp>temp_set and (temp-temp_set)<2:
        pwm_vent.ChangeDutyCycle(50)
    else:
        pwm_vent.ChangeDutyCycle(70)

try:
    while True:
        document = '/sys/bus/w1/devices/28-01889300007d/w1_slave'
        temp = read_file(document)
        temp_verschil = temp-prev_temp
        if -0.5<temp_verschil<0.5:
            prev_temp = temp
            vent_set(temp,temp_set)

except KeyboardInterrupt as e:
    print(e)

finally:
    GPIO.cleanup()
    print("Script has stopped!")
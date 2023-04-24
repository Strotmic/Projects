import serial 
ser = serial.Serial('/dev/ttyAMA0')  # open serial port 
print(ser.name)  
tekst = 'hallo'    
tekst2= tekst.encode(encoding='utf-8')   # check which port was really used 
ser.write(tekst2)     # write a string 
ser.close()             # close port
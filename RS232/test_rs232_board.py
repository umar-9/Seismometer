# https://pimylifeup.com/raspberry-pi-serial/
# Test for the RS232 connector
# Ensure to configure serial on the Pi, then restart (see link)

import time
import serial

ser = serial.Serial(
  port='/dev/ttyAM0', 
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)
counter=0


while True:
  ser.write('Write counter: %d \n'%(counter))
  time.sleep(1)
  counter += 1

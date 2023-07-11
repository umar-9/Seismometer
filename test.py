// Testing
// Ensure to enable I2C on Pi

import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Uncomment in real system - test voltages first
# ads.gain = 16 # Supposed to be 100 minimum according to the instruction manual, but only 2/3, 1, 2, 4, 8, 16 available

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads, ADS.P0) # Change pin

while True:
  print(chan.value, chan.voltage) # 12 bit (supposed to be 16 bit)

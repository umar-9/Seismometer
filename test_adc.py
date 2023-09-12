# Testing
# Ensure to enable I2C on Pi
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# ONLY USE UP TO 3V for testing
# Uncomment in real system - test voltages first
# ads.gain = 16 # Supposed to be 100 minimum according to the instruction manual, but only 2/3, 1, 2, 4, 8, 16 available

print("{:>5}\t{:>5}".format('raw', 'v'))

while True:
    print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    time.sleep(0.5)
    

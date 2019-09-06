"""
From the discussion thread: https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15/issues/27
The orignal version get the result as follow
Time of capture: 4.6360485553741455s
Sample rate is:  215.7009332529082

Modified:
1. /boot/config.txt
    dtparam=i2c_arm=on
    i2c_arm_baudrate=400000
  /home/pi/.local/lib/python3.5/site-packages/adafruit_ads1x15/ads1x15.py
          while not self._conversion_complete():
            pass  #change from time.sleep(0.01) to pass
            # time.sleep(0.01)
  pi@raspberrypi:~ $ python3 --version
    Python 3.5.3
    pi@raspberrypi:~ $ uname -a
    Linux raspberrypi 4.14.79+ #1159 Sun Nov 4 17:28:08 GMT 2018 armv6l GNU/Linux
    pi@raspberrypi:~ $ cat /proc/cpuinfo
    processor	: 0
    model name	: ARMv6-compatible processor rev 7 (v6l)
    BogoMIPS	: 697.95
    Features	: half thumb fastmult vfp edsp java tls 
    CPU implementer	: 0x41
    CPU architecture: 7
    CPU variant	: 0x0
    CPU part	: 0xb76
    CPU revision	: 7

Hardware	: BCM2835
Revision	: 9000c1
Serial		: 000000009ead533c
"""

import board
import time
import busio

i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c, data_rate=860)

# Create analog inputs for each ADXL335 axis.
#x_axis = AnalogIn(ads, ADS.P0)
#y_axis = AnalogIn(ads, ADS.P1)
z_axis = AnalogIn(ads, ADS.P2)

number_samples = 1000

samples = []

start = time.time()
for i in range(number_samples):
   samples.append(z_axis.value)

end = time.time()
total_time = end - start

print("Time of capture: {}s".format(total_time))
print("Sample rate is: ", 1000.0 / total_time)

# increasing the sampling rate 

https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15/issues/27
discussion of caternuson

I've implemented the above and pushed the working code up here:
https://github.com/caternuson/Adafruit_CircuitPython_ADS1x15/tree/fast_read
along with an example program:
https://github.com/caternuson/Adafruit_CircuitPython_ADS1x15/blob/fast_read/examples/ads1x15_fast_read.py

Testing was done on a Pi Zero W, which I realize is not the fastest Pi. Interestingly, the polling for the ready pin makes it slower than just reading a bunch of single shot conversions. Dealing with synchronization without interrupts is going to be an issue.

pi@raspberrypi:~ $ python3 ads1x15_fast_read.py 
Acquiring normal...
Time of capture: 5.0196709632873535s
Sample rate requested=860 actual=199.21624491201825
Acquiring fast...
Time of capture: 8.566477060317993s
Sample rate requested=860 actual=116.73410118988626
Acquiring fast w/o polling...
Time of capture: 1.148141860961914s
Sample rate requested=860 actual=870.9725113255598
Is this approach worth continuing to pursue? It has the following limitations:

only works for a single channel at a time
syncing the reads to conversion complete is....tricky

Since there isn't a pull request yet, easiest would be to just clone the source repo:
https://github.com/caternuson/Adafruit_CircuitPython_ADS1x15/
and switch to the fast_read branch. You can then set your PYTHONPATH environonment variable to point to that folder. This will cause that folder to be searched before the system wide folder. So it will end up using that code instead of the one installed via pip. This also means you do not need to mess with your current Python installation. No need to delete the already install library, etc.

#import dronekit_sitl
#from dronekit import connect,VehicleMode
import time
from dronekit import connect
#connect to vehicle
#sitl = dronekit_sitl.start_default()
#connection_string = sitl.connection_string()
connection_string= '/dev/ttyACM1'
vehicle = connect(connection_string, wait_ready=True)
vehicle.armed = True
while True:
	print "Read channels individually:"
	print " Ch1: %s" % vehicle.channels['1']
	print " Ch2: %s" % vehicle.channels['2']
	print " Ch3: %s" % vehicle.channels['3']
	print " Ch4: %s" % vehicle.channels['4']
	print " Ch5: %s" % vehicle.channels['5']
	print " Ch6: %s" % vehicle.channels['6']
	print " Ch7: %s" % vehicle.channels['7']
	print " Ch8: %s" % vehicle.channels['8']
	time.sleep(1)

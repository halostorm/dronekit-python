from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative

connection_string = '/dev/ttyACM0'
print('Connecting to vehicle on: %s' % connection_string)

vehicle = connect(connection_string, wait_ready=True)

def arm_and_takeoff(aTargetAltitude):

    print("Basic pre-arm checks")

    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")

    vehicle.mode = VehicleMode("GUIDED")

    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")

    vehicle.simple_takeoff(aTargetAltitude)

    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)

        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break

        time.sleep(1)

arm_and_takeoff(10)

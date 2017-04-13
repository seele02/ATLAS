import dronekit
import time

import math

from droneapi.lib import Location
from droneapi.module import api

from pymavlink import mavutil


class Flight(object):
    def __init__(self, veh_obj):
        self.Vehicle = veh_obj
        self.arm_UAV()
        self.arm_and_takeoff(35)
        time.sleep(2)
        print 'HOME:', self.Vehicle.home_location

        newLoc = Location(self.Vehicle.location.lat, self.Vehicle.location.lon, self.Vehicle.location.alt + 10)
        self.gotoGPS(newLoc)
        time.sleep(10)
        self.Vehicle.mode = self.Vehicle.mode.VehicleMode("LAND")
        self.Vehicle.flush()



    def set_mode(self):
        print 'Setting mode to Guided'
        self.Vehicle.mode = dronekit.VehicleMode("GUIDED")

    def arm_UAV(self):
        print 'Arming Now'
        print 'Current mode: ', self.Vehicle.mode
        self.Vehicle.armed = True

    def arm_and_takeoff(self, aTargetAltitude):
        """
        Arms vehicle and fly to aTargetAltitude.
        """
        vehicle = self.Vehicle
        print "Basic pre-arm checks"
        # Don't let the user try to arm until autopilot is ready
        while not vehicle.is_armable:
            print " Waiting for vehicle to initialise..."
            time.sleep(1)

        print "Arming motors"
        # Copter should arm in GUIDED mode
        vehicle.mode = dronekit.VehicleMode("GUIDED")
        vehicle.armed = True

        while not vehicle.armed:
            print " Waiting for arming..."
            time.sleep(1)

        print "Taking off!"
        vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude


        target_reached = False
        # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
        #  after Vehicle.simple_takeoff will execute immediately).
        while True:
            print " Altitude: ", vehicle.location.global_relative_frame.alt
            if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:  # Trigger just below target alt.
                print "Reached target altitude"
                target_reached = True
                break
            time.sleep(1)

        if target_reached == True:
            self.gotoGPS()




    def gotoGPS(self, location):
        vehicle = self.Vehicle
        currentLocation = vehicle.location
        targetDistance = self.get_distance_metres(currentLocation, location)
        self.gotoFunction(location)
        vehicle.flush()
        while not api.exit and vehicle.mode.name == "GUIDED":  # Stop action if we are no longer in guided mode.
            remainingDistance = self.get_distance_metres(vehicle.location, location)
            if remainingDistance <= targetDistance * 0.01:  # Just below target, in case of undershoot.
                print "Reached target"
                break
            time.sleep(2)

    def get_distance_metres(self, aLocation1, aLocation2):
        dlat = aLocation2.lat - aLocation1.lat
        dlong = aLocation2.lon - aLocation1.lon
        return math.sqrt((dlat * dlat) + (dlong * dlong)) * 1.113195e5


    def gotoFunction(self, aLocation):
        vehicle = self.Vehicle
        msg = vehicle.message_factory.set_position_target_global_int_encode(
            0,  # time_boot_ms (not used)
            0, 0,  # target system, target component
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,  # frame
            0b0000111111111000,  # type_mask (only speeds enabled)
            aLocation.lat * 1e7,  # lat_int - X Position in WGS84 frame in 1e7 * meters
            aLocation.lon * 1e7,  # lon_int - Y Position in WGS84 frame in 1e7 * meters
            aLocation.alt,
            # alt - Altitude in meters in AMSL altitude, not WGS84 if absolute or relative, above terrain if GLOBAL_TERRAIN_ALT_INT
            0,  # X velocity in NED frame in m/s
            0,  # Y velocity in NED frame in m/s
            0,  # Z velocity in NED frame in m/s
            0, 0, 0,  # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
            0, 0)  # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
        # send command to vehicle
        vehicle.send_mavlink(msg)
        vehicle.flush()




    def get_mode(self):
        return self.Vehicle.mode

    def get_armed(self):
        return self.Vehicle.armed

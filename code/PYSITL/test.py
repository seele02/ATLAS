import dronekit_sitl
import time
from dronekit import connect
from dronekit import VehicleMode
from solo_connect import connect as solo_connect


#vehicle = connect('127.0.0.1:14550', wait_ready=True)

import dronekit
import socket
import exceptions


class test(object):



    def conn(self):
        self.height = 50
        self.mode = 'AUTO'
        #vehicle = dronekit.connect('127.0.0.1:14550', heartbeat_timeout=15)
        vehicle = solo_connect().ip('127.0.0.1', '14550', 5)


        print vehicle.mode
        if vehicle:
            vehicle.mode = VehicleMode("GUIDED")
        while vehicle.armed == False:
            if vehicle.armed == False:
                vehicle.armed = True

        print vehicle.armed
        if vehicle.armed == True:
            time.sleep(3)
            vehicle.simple_takeoff(self.height)


        #vehicle.mode == 'LOITER'



        while vehicle.mode == 'GUIDED':
            aug = (vehicle.location._down*-1)/(self.height)
            print 'AUG: ', aug
            print vehicle.mode
            print vehicle.location._down
            time.sleep(1)

            if aug > 0.99:
                print '* * * Landing Now * * *: ', aug

                #time.sleep(10)
                while vehicle.mode == 'GUIDED':
                    vehicle.mode == 'LAND'


test().conn()

import dronekit_sitl
import time
from dronekit import connect
from dronekit import VehicleMode
import dronekit
from solo_connect import connect as solo_connect

class UAV(object):
    def __init__(self):
        self.height = 50
        self.mode = None
        self.vehicle = self.conn()


    def conn(self):
        veh_conn = solo_connect()
        try:
            vehicle = veh_conn.ip('127.0.0.1', '14550', 5)
        except:
            print 'CAUGHT!'
            raise

        exceptions = veh_conn.get_exceptions()
        if len(exceptions):
            i = len(exceptions)
            for i in exceptions:
                print 'EXCEPTION(',exceptions.index(i), '): ', i

        messages = veh_conn.get_message()
        if len(messages):
            i = len(messages)
            for i in messages:
                print 'MESSAGE(',messages.index(i), '): ', i
        if vehicle:
            return vehicle






    def setMode(self, mode_string):

        if self.vehicle:
            old_mode = self.vehicle.mode
            self.vehicle.mode = VehicleMode(str(mode_string))
            self.mode = VehicleMode(str(mode_string))
            if self.vehicle.mode == self.mode:
                if self.vehicle.mode != old_mode:
                    print 'MODE CHANGED TO', mode_string, ' from ', old_mode.name
            else:
                print 'WARNING: Mode mismatch'
        else:
            print 'FATAL ERROR: No Vehicle Available'
            exit()


    def mode_armable(self):


        self.vehicle.armed = True



        if self.vehicle.on_message('Mode not armable'):
            print self.vehicle.mode.name
            return False
        else:
            return True








    def arm_vehicle(self):
        print 'Armable:', self.vehicle.is_armable
        print 'Armed: ', self.vehicle.armed
        print 'Mode Armable: ', self.mode_armable()



        '''
        if self.vehicle.is_armable == True:
            while self.vehicle.armed == False:
                try:
                    self.vehicle.armed = True
                except:
                    raise
                if self.vehicle.armed == True:
                    pass
        '''


    def test(self):
        print self.vehicle.mode
        if self.vehicle:
            self.vehicle.mode = VehicleMode("GUIDED")


        print self.vehicle.armed
        if self.vehicle.armed == True:
            time.sleep(3)
            self.vehicle.simple_takeoff(self.height)


        #vehicle.mode == 'LOITER'



        while self.vehicle.mode == 'GUIDED':
            aug = (self.vehicle.location._down*-1)/(self.height)
            print 'AUG: ', aug
            print self.vehicle.mode
            print self.vehicle.location._down
            time.sleep(1)

            if aug > 0.99:
                print '* * * Landing Now * * *: ', aug

                #time.sleep(10)
                if self.vehicle.mode == VehicleMode("GUIDED"):
                    self.vehicle.mode = VehicleMode("LAND")


class takeoff():
    def __init__(self, vehicle):
        self.vehicle = vehicle


    #def set_altitude(self, alt):








t = UAV()
#t.start_SITL()
#t.conn()
#t.setMode('GUIDED')
#t.arm_vehicle()



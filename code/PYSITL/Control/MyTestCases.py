import dronekit_sitl
import time
from dronekit import connect
from dronekit import VehicleMode
import dronekit
from pymavlink import mavutil

from solo_connect import connect as solo_connect

class UAV(object):
    def __init__(self):
        self.height = None
        self._mode = None
        self._vehicle = None
        self._veh_ip = None
        self._veh_port = None
        self._veh_timeout = None

    def default_setup(self):
        self.ip = '127.0.0.1'
        self.port = '14550'
        self.timeout= 5

    @property
    def vehicle(self):
        return self._vehicle

    @vehicle.setter
    def vehicle(self, connection_type):
        if connection_type == 'default':
            self.default_setup()
        self.vehicle = self.get_conn(self.ip, self.port, self.timeout)


    @property
    def ip(self):
        return self._veh_ip

    @ip.setter
    def ip(self, ip):
        self._veh_ip = ip

    @property
    def port(self):
        return self._veh_port

    @port.setter
    def port(self, port):
        self._veh_port = port


    @property
    def timeout(self):
        return self._veh_timeout

    @timeout.setter
    def timeout(self, time_in_seconds):
        assert isinstance(time_in_seconds, int)
        self._veh_timeout = time_in_seconds

    def get_conn(self, ip, port, timeout):
        veh_conn = solo_connect()
        try:
            vehicle = veh_conn.ip(ip, port, timeout)
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





    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode_string):

        if self.vehicle:
            old_mode = self.vehicle.mode
            self.vehicle.mode = VehicleMode(str(mode_string))
            self._mode = VehicleMode(str(mode_string))
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





new_UAV = UAV()
vehicle = new_UAV.vehicle

print new_UAV.ip
print new_UAV.port
print new_UAV.timeout

new_UAV.mode = vehicle.mode
print new_UAV
#t.start_SITL()
#vehicle = new_UAV.vehicle
#cmds = vehicle.commands
#cmds.add(
    #dronekit.Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 0, 10))

#point1 = get_location_metres(aLocation, aSize, -aSize)

#print cmds.count
#cmds.clear()
#t.setMode('GUIDED')
#t.arm_vehicle()



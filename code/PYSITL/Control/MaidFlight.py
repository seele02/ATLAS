class MaidFlight(object):
    def __init__(self, sim):
        '''
        self.start_long = self.query_value('Starting Longitude', val_type='lon')
        self.start_lat = self.query_value('Starting Latitude', val_type='lat')
        self.dest_long = self.query_value('Destination Longitude', val_type='lon')
        self.dest_lat = self.query_value('Destination Longitude', val_type='lat')

        print self.start_long
        print self.start_lat
        print self.dest_long
        print self.dest_lat'''




        if sim ==  True:
            Flight_Start('127.0.0.1', '14550', 5)


    def query_value(self, val_string, val_type):
        import re
        p = None
        if val_type is 'lat':
            p = re.compile('^-?([1-8]?[1-9]|[1-9]0)\.{1}\d{1,6}')
        elif val_type is 'lon':
            p = re.compile('^-?([1]?[1-7][1-9]|[1]?[1-8][0]|[1-9]?[0-9])\.{1}\d{1,6}')

        user_choice = raw_input("Enter "+ str(val_string)+ ": ")
        swap = None
        if p:
            if user_choice:
                if p.match(user_choice):
                    print 'Match'
                    swap = self.float_conversion(user_choice)
                else:
                    print 'No Match'
                    swap = self.query_value(val_string, val_type)

            else:
                print 'Please enter a value'
                swap = self.query_value(val_string, val_type)
        else:
            print 'Regex not set'

        if swap:
            return swap


    def float_conversion(self, user_choice):
        try:
            to_flt = float(user_choice)
            print to_flt, ' : ', type(to_flt)
            return to_flt
        except:
            print 'FLOAT CONVERSION ERROR'


import MyTestCases
class Flight_Start(object):
    def __init__(self, ip, port, timeout):
        #self.flight = MyTestCases.connect(ip, port, timeout)

        new_UAV = MyTestCases.UAV()
        new_UAV.default_setup()

        print 'Before: ', new_UAV._vehicle
        new_UAV.conn()
        print 'After: ',new_UAV._vehicle
        self.globvehicle = new_UAV.get_conn()
        #vehicle = new_UAV.vehicle

        if self.globvehicle:
            self.get_telemetry()




    def get_telemetry(self):
        #dronekit.LocationLocal.__str__()
        new_dict = dict()
        new_dict['Global Location'] = self.globvehicle.location.global_frame.__str__()
        new_dict['Local Location'] = self.globvehicle.location.local_frame.__str__()
        new_dict['Attitude'] = self.globvehicle.attitude.__str__()
        new_dict['Velocity'] = self.globvehicle.velocity
        new_dict['GPS'] = self.globvehicle.gps_0.__str__()
        new_dict['Groundspeed'] = self.globvehicle.groundspeed
        new_dict['Airspeed'] = self.globvehicle.airspeed
        new_dict['Gimbal status'] = self.globvehicle.__str__()
        new_dict['Battery'] = self.globvehicle.battery.__str__()
        new_dict['EKF OK?'] = self.globvehicle.ekf_ok
        new_dict['Last Heartbeat'] = self.globvehicle.last_heartbeat
        new_dict['Rangefinder'] = self.globvehicle.rangefinder.__str__()
        new_dict['Rangefinder distance'] = self.globvehicle.rangefinder.distance
        new_dict['Rangefinder voltage'] = self.globvehicle.rangefinder.voltage
        new_dict['Heading'] = self.globvehicle.heading
        new_dict['Is Armable'] = self.globvehicle.is_armable
        new_dict['System status'] = self.globvehicle.system_status.state
        new_dict['Mode'] = self.globvehicle.mode.name
        new_dict['Armed'] = self.globvehicle.armed

        print new_dict



        #print "Global Location: %s" % self.globvehicle.location.global_frame
        #print "Global Location (relative altitude): %s" % globvehicle.location.global_relative_frame
        #print "Local Location: %s" % globvehicle.location.local_frame  # NED
        #print "Attitude: %s" % globvehicle.attitude
        #print "Velocity: %s" % globvehicle.velocity
        #print "GPS: %s" % globvehicle.gps_0
        #print "Groundspeed: %s" % globvehicle.groundspeed
        #print "Airspeed: %s" % globvehicle.airspeed
        #print "Gimbal status: %s" % globvehicle.gimbal
        #print "Battery: %s" % globvehicle.battery
        #print "EKF OK?: %s" % globvehicle.ekf_ok
        #print "Last Heartbeat: %s" % globvehicle.last_heartbeat
        #print "Rangefinder: %s" % globvehicle.rangefinder
        #print "Rangefinder distance: %s" % globvehicle.rangefinder.distance
        #print "Rangefinder voltage: %s" % globvehicle.rangefinder.voltage
        #print "Heading: %s" % globvehicle.heading
        #print "Is Armable?: %s" % globvehicle.is_armable
        #print "System status: %s" % globvehicle.system_status.state
        #print "Mode: %s" % globvehicle.mode.name  # settable
        #print "Armed: %s" % globvehicle.armed  # settable






t = MaidFlight(sim=True)

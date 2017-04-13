import time
import dronekit

global globvehicle

def get_vehicle():
    pass

class Menu(object):
    def __init__(self, banner, choice_array):
        self._set_choice_array(choice_array)

        self.key_val_choice = dict()
        self.set_choice_numbering()

        self.banner_display = banner
        self.choice_array = self.get_choice_array()
        self.print_display_banner()
        self.choice = self._iterate_choices()
        self.single = None
        self._set_zero_val()

        print '[ USER CHOICE: ', self.choice, ' ]'

    def add_sing(self, single):
        if not self.single:
            self.single = single

    def _set_zero_val(self):
        if int(self.choice) == 0:
            print '[ EXITING ]'
            exit()

    def _set_choice_array(self, choice_array):
        self.choice_array = choice_array

    def set_choice_numbering(self):
        self.key_val_choice[0] = 'EXIT'
        for index in range(self.get_choice_count()):
            self.key_val_choice[index + 1] = self.choice_array[index]

    def get_choice_array(self):
        return self.choice_array

    def get_choice_count(self):
        choice_num = 0
        try:
            choice_num = len(self.choice_array)
        except:
            raise
        finally:
            return choice_num

    def get_display_banner(self):
        return "\n\n*************************************\n", \
               str(self.banner_display), \
               "\n*************************************"

    def print_display_banner(self):
        print "\n\n*************************************\n", \
            str(self.banner_display), \
            "\n*************************************"


    def _iterate_choices(self):
        for key, value in self.key_val_choice.iteritems():  # for each index in the choice_array argument
            # print the index as a sting and the corresponding index of the choice array
            print str(key) , '. ' , str(value)

        # store the raw_input(as opposed to input which doesn't always store as a string) as user_choice
        user_choice = raw_input("Type the number the corresponds to the process that you"
                                " would like to complete from the list above: ")

        try:  # try block
            # if user_choice(onverted to an integer) is out of the bounds of the array
            if (int(user_choice) < self.get_choice_count()+1):
                if (int(user_choice) >= int(0)):  # if user_choice(onverted to an integer) is out of the bounds of the array
                    return int(user_choice)  # return user_choice as an integer
                else:
                    print "\n[ *****Number Chosen Must be Greater than 0***** ]\n"
                    return self._iterate_choices()  # recursive module call
            else:
                print "\n[ *****Number Chosen Out of Bounds***** ]\n"
                return self._iterate_choices()  # recursive module call
        except (IndexError, ValueError):  # catch Index out of bounds & Non-numeric value
            print "\n[ *****Please select a valid number***** ]\n"
            return self._iterate_choices()  # recursive module call


    def get_class(self):
        return self


class Sub_Menu(Menu):
    def __init__(self, banner, choice_array):
        super(Sub_Menu, self).__init__(banner, choice_array)
        #self.parent_menu = parent_menu
        self.set_choice_numbering()
        self._set_zero_val()

    def set_choice_numbering(self):
        self.key_val_choice[0] = 'BACK'
        for index in range(self.get_choice_count()):
            self.key_val_choice[index + 1] = self.choice_array[index]

    def _set_zero_val(self):
        if int(self.choice) == 0:
            print '[ Go Back ]'



def main_menu():
    m = Menu('Main Menu', choice_array=["UAV", "Sensors", "Database", "Etc."])
    print m.choice

    if m.choice == 1:
        print m
        sub_menu_UAV()
    else:
        pass

def sub_menu_UAV():

    choice_array = ["Connect to Simulated UAV", "Get UAV status", "Mission"]
    global globvehicle
    while(1):
        s = Sub_Menu("TEST", choice_array=choice_array)
        choice = s.choice
        if choice == 0:
            #origin._iterate_choices()
            main_menu()
        elif choice == 1:
            from code.PYSITL.Control import solo_connect
            c = solo_connect.connect().ip('127.0.0.1', '14550', 5)
            if c:
                globvehicle = c
                th = threading.Thread(target=threadFunc)
                th.daemon = True
                th.start()
                print "Daemon Started"
                print "Glob Vehicle Param set as: ", globvehicle
            else:
                print "Error: Connection failed"
            #c = threading.Thread(target=solo_connect.connect().ip('127.0.0.1', '14550', 5))
            #c.start()
        elif choice == 2:
                try:
                    if globvehicle:
                        print '***VEHICLE***: ', globvehicle
                        print "Autopilot Firmware version: %s" % globvehicle.version
                        print "Autopilot capabilities (supports ftp): %s" % globvehicle.capabilities.ftp
                        print "Global Location: %s" % globvehicle.location.global_frame
                        print "Global Location (relative altitude): %s" % globvehicle.location.global_relative_frame
                        print "Local Location: %s" % globvehicle.location.local_frame  # NED
                        print "Attitude: %s" % globvehicle.attitude
                        print "Velocity: %s" % globvehicle.velocity
                        print "GPS: %s" % globvehicle.gps_0
                        print "Groundspeed: %s" % globvehicle.groundspeed
                        print "Airspeed: %s" % globvehicle.airspeed
                        print "Gimbal status: %s" % globvehicle.gimbal
                        print "Battery: %s" % globvehicle.battery
                        print "EKF OK?: %s" % globvehicle.ekf_ok
                        print "Last Heartbeat: %s" % globvehicle.last_heartbeat
                        print "Rangefinder: %s" % globvehicle.rangefinder
                        print "Rangefinder distance: %s" % globvehicle.rangefinder.distance
                        print "Rangefinder voltage: %s" % globvehicle.rangefinder.voltage
                        print "Heading: %s" % globvehicle.heading
                        print "Is Armable?: %s" % globvehicle.is_armable
                        print "System status: %s" % globvehicle.system_status.state
                        print "Mode: %s" % globvehicle.mode.name  # settable
                        print "Armed: %s" % globvehicle.armed  # settable
                        cmds = globvehicle.commands
                        while not globvehicle.home_location:

                            cmds.download()
                            cmds.wait_ready()
                            if not globvehicle.home_location:
                                print " Waiting for home location ..."
                                time.sleep(4)
                        for cmd in cmds:
                            print cmd
                        print 'Home: ', globvehicle.home_location

                except UnboundLocalError:
                    print '[Unbound Local Error]: No Connection \nMake sure you have connected to the UAV first'
                except TypeError:
                    print 'Type Error'
                except dronekit.APIException:
                    print 'UAV Exception'

                except NameError:
                    print '[Name Error]: No Connection \nMake sure you have connected to the UAV first'
        elif choice == 3:
            sub_menu_UAV_Mission_Generation()

            #c = threading.Thread(target=solo_connect.connect().ip('127.0.0.1', '14550', 5))
            #c.start()


def sub_menu_UAV_Mission_Generation():

    choice_array = ["List Current waypoints", "Get UAV location"]
    global globvehicle
    while(1):
        s = Sub_Menu("TEST", choice_array=choice_array)
        choice = s.choice
        if choice == 0:
            #origin._iterate_choices()
            sub_menu_UAV()
        elif choice == 1:
            try:
                if globvehicle:
                    cmds = globvehicle.commands
                    cmds.download()
                    cmds.wait_ready()
                    for cmd in cmds:
                        print cmd
            except UnboundLocalError:
                print 'Make sure you have connected to the UAV first'
            except TypeError:
                print 'Type Error'
        elif choice == 2:
                try:

                    home = []
                    curr_location = []
                    cmds = globvehicle.commands
                    while not globvehicle.home_location:

                        cmds.download()
                        cmds.wait_ready()
                        if not globvehicle.home_location:
                            print " Waiting for home location ..."
                            time.sleep(4)
                    print 'Home: ', globvehicle.home_location.lat
                    if globvehicle.location.global_relative_frame:
                        home.append(globvehicle.home_location.lat)
                        home.append(globvehicle.home_location.lon)
                        home.append(globvehicle.home_location.alt)
                    if globvehicle.location.global_frame:
                        curr_location.append(globvehicle.location.global_frame.lat)
                        curr_location.append(globvehicle.location.global_frame.lon)
                        curr_location.append(globvehicle.location.global_frame.alt)


                    for i in range(len(home)):
                        print home[i], ' : ', curr_location[i]
                        if home[i] % curr_location[i] < 0.000001:
                            print 'check'


                except UnboundLocalError:
                    print 'Make sure you have connected to the UAV first'
                except IndexError:
                    print 'Home location not initialized'

            #c = threading.Thread(target=solo_connect.connect().ip('127.0.0.1', '14550', 5))
            #c.start()



import threading

def threadFunc():
    while True:
        time.sleep(10)
        global globvehicle
        print "\nLast Heartbeat: %s" % globvehicle.last_heartbeat
        print globvehicle



while(1):
    main_menu()

globvehicle.close()
'''
Description: Displays choices generated from array of sting args

'''

class Menu(object):
    def __init__(self, banner, choice_array):
        self._set_choice_array(choice_array)

        self.key_val_choice = dict()
        self.set_choice_numbering()

        self.banner_display = banner
        self.choice_array = self.get_choice_array()
        self.print_display_banner()
        choice = self._iterate_choices()
        print '[ USER CHOICE: ', choice, ' ]'

        if int(choice) == 0:
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
        user_choice = raw_input(
            "Type the number the corresponds to the process that you would like to complete from the list above: ")

        try:  # try block
            # if user_choice(onverted to an integer) is out of the bounds of the array
            if (int(user_choice) < self.get_choice_count()+1):
                # return user_choice as an integer
                return int(user_choice)
            else:
                print "\n[ *****Number Chosen Out of Bounds***** ]\n"
                return self._iterate_choices()  # recursive module call
        except (IndexError, ValueError):  # catch Index out of bounds & Non-numeric value
            print "\n[ *****Please select a valid number***** ]\n"
            return self._iterate_choices()  # recursive module call


class ChoiceFunctionLink(object):
    def __init__(self, num_choice_dict):

        self.num_choice_dict = dict(num_choice_dict)
        self.choice_function_dict = dict()

        #print self.num_choice_dict.itervalues()

    def link_function(self, value, function, *args):

        if self.in_dict(value):
            #runs the function using additional args
            link = LinkFunction(function, *args)
            self.choice_function_dict[value] = link
            #Execute Function with arguments
            #functioncp(*argscp)

        else:
            print 'Given Choice option is invalid'


    def funtion_excecute(self, value):
        if self.in_dict(value):
            test = LinkFunction(self.choice_function_dict[value]).function
            print 'Executing: ', test
            test.execute()


        else:
            print 'Given Choice option is not in queue'



    def in_dict(self, value):
        if value in self.num_choice_dict.itervalues():
            return True
        else:
            return False




class LinkFunction(object):
    def __init__(self, function, *args):
        self.function = function
        self.args = args

    def get_value_pair(self):
        val_dict = dict()
        val_dict[self.function] = self.args
        return val_dict

    def get_function(self):
        return self.function

    def get_args(self):
        return self.args

    def execute(self):
        this_args = self.args
        self.function(*this_args)

    def __str__(self):
        string = self.get_value_pair()
        return string.__str__()






t = Menu('Main Menu', choice_array=["Compute", "Storage", "AWS Monitor", "Elastic Load Balancing"])
#t._iterate_choices() #Already in __init__(), DON'T CALL MANUALLY ! ! !

new_dict = dict()
new_dict[0] = 'EXIT'
new_dict[1] = 'Compute'
new_dict[2] = 'Storage'
new_dict[3] = 'AWS Monitor'
new_dict[4] = 'Elastic Load Balancing'

c = ChoiceFunctionLink(new_dict)
import solo_connect
#import MyTestCases as UAVClass


c.link_function('Storage', solo_connect.connect().ip, '127.0.0.1', '14550', 5)
c.link_function('Compute', solo_connect.connect().get_test, 'My Test')
#c.link_function('Compute', UAVClass.UAV)
print c.choice_function_dict
#c.funtion_excecute('Storage')
c.funtion_excecute('Compute')



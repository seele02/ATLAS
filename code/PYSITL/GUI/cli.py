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


class ChoiceFunctionLink(dict):
    def __init__(self, num_choice_dict, **kwargs):
        super(ChoiceFunctionLink, self).__init__(**kwargs)
        self.num_choice_dict = dict(num_choice_dict)
        self.choice_function_dict = dict()

        print self.num_choice_dict.itervalues()

    def add_link(self, value, function, *args):
        if self.in_dict(value):
            print 'DO'
            #runs the function using additional args
            fun = function

            print fun, " : ", args
            fun(*args)

            print args
            #fun(args[0], args[1], args[2])
            #self.choice_function_dict[value] =
        else:
            print 'Given Choice option is invalid'




    def in_dict(self, value):
        if value in self.num_choice_dict.itervalues():
            return True
        else:
            return False





#t = Menu('Main Menu', choice_array=["Compute", "Storage", "AWS Monitor", "Elastic Load Balancing"])
#t._iterate_choices() #Already in __init__(), DON'T CALL MANUALLY ! ! !

new_dict = dict()
new_dict[0] = 'EXIT'
new_dict[1] = 'Compute'
new_dict[2] = 'Storage'
new_dict[3] = 'AWS Monitor'
new_dict[4] = 'Elastic Load Balancing'

c = ChoiceFunctionLink(new_dict)
import solo_connect


c.add_link('Storage', solo_connect.connect().ip, '127.0.0.1', '14550', 5)
print c.choice_function_dict

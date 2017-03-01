import dronekit
import socket
import exceptions


class connect:
    def __init__(self):
        self.__message = []
        self.__exceptions = []


    def ip(self, ip, port, timeout):

        print 'Connecting via IP'

        vehicle = None

        ip_in = str(ip)
        port_in = str(port)
        timeout = int(timeout)

        ip_concat = ip_in + ':' + port_in

        print ip_concat

        try:
            vehicle = dronekit.connect(ip_concat, heartbeat_timeout=timeout)

        # Bad TCP connection
        except socket.error as e:
            self.__set_message('Error(1): Unable to connect to Server')
            self.__set_exceptions(Exception(e))
            raise


        # Bad TTY connection
        except exceptions.OSError as e:

            self.__set_message('Error(2): Unable to connect to serial Port')
            self.__set_exceptions(Exception(e))
            raise


        # API Error
        except dronekit.APIException as e:
            self.__set_message('Error(3): MAVLink Connection Timeout')
            self.__set_exceptions(Exception(e))
            raise



        # Other error
        except:
            self.__set_message('Some other error!')
            self.__set_exceptions('???')
            raise


        return vehicle




        '''
        try:
            vehicle = dronekit.connect(ip_concat, heartbeat_timeout=timeout)

        # Bad TCP connection
        except socket.error:
            self.__set_message('Error(1): Unable to connect to Server')
            self.__set_exceptions(Exception(socket.error))


        # Bad TTY connection
        except exceptions.OSError as e:

            self.__set_message('Error(2): Unable to connect to serial Port')
            self.__set_exceptions(Exception(e))


        # API Error
        except dronekit.APIException as e:
            self.__set_message('Error(3): MAVLink Connection Timeout')
            self.__set_exceptions(Exception(e))



        # Other error
        except:
            self.__set_message('Some other error!')
            self.__set_exceptions('???')


        return vehicle
        '''
    def __set_message(self, message):
        self.__message.append(message)

    def __set_exceptions(self, exception):
        self.__exceptions.append(exception)

    def get_message(self):
        return self.__message

    def get_exceptions(self):
        return self.__exceptions

    def get_test(self, my_test):
        print 'EXECUTION SCRIPT INIT!!'
        return my_test

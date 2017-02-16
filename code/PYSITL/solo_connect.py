import dronekit
import socket
import exceptions


class connect:
    def __init__(self):
        print 'Connecting'


    def ip(self, ip, port, timeout):

        print 'via IP'

        ip_in = str(ip)
        port_in = str(port)
        timeout = int(timeout)

        ip_concat = ip_in + ':' + port_in

        print ip_concat

        try:
            vehicle = dronekit.connect(ip_concat, heartbeat_timeout=timeout)

        # Bad TCP connection
        except socket.error:
            print 'Error(1): Unable to connect to Server'
            raise

        # Bad TTY connection
        except exceptions.OSError as e:
            print 'Error(2): Unable to connect to serial Port'
            raise

        # API Error
        except dronekit.APIException:
            print 'Error(3): MAVLink Connection Timeout'
            raise

        # Other error
        except:
            print 'Some other error!'
            raise

        return vehicle
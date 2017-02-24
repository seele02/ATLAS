
def iterate_choices(choice_array):
    for index in range(len(choice_array)):  #for each index in the choice_array argument
        print str(index) + '. ' + choice_array[index] #print the index as a sting and the corresponding index of the choice array
    user_choice = raw_input("Type the number the corresponds to the process that you would like to complete from the list above: ") #store the raw_input(as opposed to input which doesn't always store as a string) as user_choice
    try: #try block
        if(int(user_choice)<len(choice_array)): #if user_choice(onverted to an integer) is out of the bounds of the array
            return int(user_choice) #return user_choice as an integer
        else:
            print "\n[ *****Number Chosen Out of Bounds***** ]\n"
            return iterate_choices(choice_array) #recursive module call
    except (IndexError, ValueError): #catch Index out of bounds & Non-numeric value
        print "\n[ *****Please select a valid number***** ]\n"
        return iterate_choices(choice_array) #recursive module call


def main_menu():
    banner_display("\t\t\t\tMain")
    choice_array = ["<EXIT>",
                    "Compute",
                    "Storage",
                    "AWS Monitor",
                    "Elastic Load Balancing",
                    ] #create an array of user choices
    choice = iterate_choices(choice_array) #call the choice iterator with the array as an argument
    if choice == 0:
        exit() #exit the program
    elif choice == 1:
        sub_menu("compute") #call the AWS/OpenStack chooser an 'origin' option is added so later itterations know which method to call
    elif choice == 2:
        sub_menu("storage") #call the AWS/OpenStack chooser
    elif choice == 3:
        monitor_AWS() #calls monitoring module
    elif choice == 4:
        elastic_load_balancing() #calls my chosen option (Elastic load balancing)

def sub_menu(origin):

    choice_array = ["<BACK>", "AWS", "OpenStack"]
    choice = iterate_choices(choice_array)
    if choice == 0:
        main_menu() #goes back to originating method
    if origin == "compute": #if the origin parameter is from compute section
        if choice == 1:
            compute_AWS() #AWS compute method
        elif choice == 2:
            compute_openstack() #openstack compute method
    elif origin == "storage": #if the origin parameter is from compute section
        if choice == 1:
            storage_AWS() #AWS storage method
        elif choice == 2:
            storage_openstack() #openstack torage method

def compute_AWS():
    print "\n\n*************************************\n" \
              "               AWS Compute" \
              "\n*************************************"

    choice_array = ["<BACK>", "List all Running Instances", "See Info on Specific Index",
                           "Start a stopped Instance", "Stop all Instances", "Stop running Instance",
                           "Attach existing volume", "Detach volume", "Launch new instance"]
    choice = iterate_choices(choice_array)
    #ec2inst = EC2Instance() #Create a new EC2Instance
    if choice == 0:
        sub_menu("compute") #Calls previous method (shows necesity of origin argument)
    elif choice == 1:
        print '\n*****Running Instances*****'
        #ec2inst.list_instances(True) #calls the list_instance function in the ec2Instance (True Argument is for verbosity option, explained later)
    elif choice == 2:
        pass
        #ec2inst.get_instance_info()
    elif choice == 3:
        pass
        #ec2inst.start_stopped_instance()
    elif choice == 4:
        pass
        #ec2inst.stop_all()
    elif choice == 5:
        pass
        #ec2inst.stop_instance()
    elif choice == 6:
        pass
        #ec2inst.attach_existing_volume()
    elif choice == 7:
        pass
        #ec2inst.detach_volume()
    elif choice == 8:
        pass
        #ec2inst.start_new_instance()
    compute_AWS()


    '''Rest of class is pretty much self explanitory/repeated'''


def compute_openstack():
    print "\n\n*************************************\n" \
              "               OpenStack Compute" \
              "\n*************************************"
    choice_array = ["<BACK>", "List all Running Instances"]
    choice = iterate_choices(choice_array)
    if choice == 0:
        sub_menu("compute")
    elif choice == 1:
        pass
        #openstack_inst = Nova.list_running()
        #openstack_inst.list_nodes()
    compute_openstack()

def storage_AWS():
    print "\n\n*************************************\n" \
              "               S3 Storage" \
              "\n*************************************"
    choice_array = ["<BACK>", "List all Buckets", "List Objects in Bucket", "Upload Object",
                    "Download an Object from Bucket", "Delete an Object in Bucket"]
    choice = iterate_choices(choice_array)
    print '[ SELECTED: ' + str(choice_array[choice]), ' ]\n'
    #s3inst = S3Instance()
    if choice == 0:
        sub_menu("storage")
    elif choice == 1:
        pass
        #s3inst.list_all_buckets(True)
    elif choice == 2:
        pass
        #s3inst.list_all_objects_in_bucket()
    elif choice == 3:
        pass
        #s3inst.upload_to_a_bucket()
    elif choice == 4:
        pass
        #s3inst.download_from_bucket()
    elif choice == 5:
        pass
        #s3inst.delete_object_from_bucket()
    storage_AWS()

def storage_openstack():
    print "\n\n*************************************\n" \
              "          OpenStack Storage" \
              "\n*************************************"
    choice_array = ["<BACK>", "List all Containers", "List Objects in Containers", "Upload Object",
                    "Download an Object from Containers", "Delete an Object in Containers"]
    choice = iterate_choices(choice_array)
    print '[ SELECTED: ' + str(choice_array[choice]), ' ]\n'
    #swift_inst = SwiftInstance()
    if choice == 0:
        sub_menu("storage")
    elif choice == 1:
        pass
        #swift_inst.list_all_containers(True)
    elif choice == 2:
        pass
        #swift_inst.list_objects_in_container()
    elif choice == 3:
        print
    elif choice == 4:
        print
        #compute_stop_all_instances()
    elif choice == 5:
        print
    storage_openstack()

def monitor_AWS():
    print "\n\n*************************************\n" \
              "            Monitor AWS (CloudWatch)" \
              "\n*************************************"

    choice_array = ["<BACK>", "List all Metrics for an Instance", "Create an Alarm if CPU Usage drops below 40%"]
    choice = iterate_choices(choice_array)
    print '[ SELECTED: ' + str(choice_array[choice]), ' ]\n'
    #cw_inst = CloudWatchInstance()
    if choice == 0:
        main_menu()
    elif choice == 1:
        pass
        #cw_inst.list_metrics()
    elif choice == 2:
        pass
        #cw_inst.less_than_40_alarm()
    monitor_AWS()


def elastic_load_balancing():
    banner_display("Elastic Load Balancing")

    choice_array = ["<BACK>", "See Running Load Balancers", "Create a new Load Balancer", "Delete Existing Load Balancer"]
    choice = iterate_choices(choice_array)
    print '[ SELECTED: ' + str(choice_array[choice]), ' ]\n'
    #elb_inst = elb_instance()
    if choice == 0:
        main_menu()
    elif choice == 1:
        pass
        #elb_inst.list_all_load_balancers(True)
    elif choice == 2:
        pass
        #elb_inst.create_new_load_balancer()
    elif choice == 3:
        pass
        #elb_inst.delete_existing_load_balancer()
    elastic_load_balancing()


def banner_display(title):
    print "\n\n*************************************\n",\
        str(title),\
        "\n*************************************"


main_menu()


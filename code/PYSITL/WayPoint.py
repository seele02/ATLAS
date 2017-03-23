class WayPoint():
    def __init__(self, index, command, longitude, latitude, altitude, auto_continue):
        self.index = index
        self.current_wp = 0
        self.coord_frame = 0
        self.command = command
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.p4 = 0
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
        self.auto_continue = auto_continue

    def __str__(self):
        collection = [self.index, self.current_wp, self.coord_frame, self.command, self.p1, self.p2, self.p3, self.p4, self.longitude, self.latitude, self.altitude, self.auto_continue]
        string = ''
        for item in collection:
            string += item.__str__() + '\t'
        return string


t = WayPoint(0, 179, 52, 65, 30, 0)
print t
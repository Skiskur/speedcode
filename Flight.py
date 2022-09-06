from datetime import datetime


class Flight:
    def __init__(self, flight_no, origin, destination, departure: str, arrival: str, base_price, bag_price,
                 bags_allowed: str):
        self.flight_no = flight_no
        self.origin = origin
        self.destination = destination
        self.departure = datetime.strptime(departure, '%Y-%m-%dT%H:%M:%S')
        self.arrival = datetime.strptime(arrival, '%Y-%m-%dT%H:%M:%S')
        self.base_price = float(base_price)
        self.bag_price = float(bag_price)
        self.bags_allowed = int(bags_allowed)

    def get_time(self):
        return self.arrival - self.departure

    def print(self):
        print("\t###############################")
        print("\t\"flight_no\":", self.flight_no)
        print("\t\"origin\":", self.origin)
        print("\t\"destination\":", self.destination)
        print("\t\"departure\":", self.departure)
        print("\t\"arrival\":", self.arrival)
        print("\t\"base_price\":", self.base_price)
        print("\t\"bag_price\":", self.bag_price)
        print("\t\"bags_allowed\":", self.bags_allowed)
        print("\t###############################")
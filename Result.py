import Flight
from datetime import timedelta


class Result:
    def __init__(self, origin="", destination="", bags_count=0):
        self.flights = []
        self.origin = origin
        self.destination = destination
        self.bags_allowed = int(bags_count)
        self.bags_count = int(bags_count)
        self.total_price = float(0)
        self.travel_time = timedelta(hours=0)
        self.current_location = origin
        self.current_time = 0
        self.visited = []

    def add_flight(self, flight: Flight):
        self.flights.append(flight)
        self.visited.append(self.current_location)
        self.total_price += flight.base_price + (flight.bag_price * self.bags_count)
        self.current_time = flight.arrival
        self.current_location = flight.destination
        self.travel_time += flight.get_time()

    def copy(self, r):
        self.flights = r.flights.copy()
        self.origin = r.origin
        self.destination = r.destination
        self.bags_allowed = r.bags_allowed
        self.bags_count = r.bags_count
        self.total_price = r.total_price
        self.travel_time = r.travel_time
        self.current_location = r.current_location
        self.current_time = r.current_time
        self.visited = r.visited.copy()


    def print(self):
        print("--------------------------------")
        # for flight in self.flights:
        #     flight.print()
        print(len(self.flights))
        print("\"bags_allowed\":", self.bags_allowed)
        print("\"bags_count\":", self.bags_count)
        print("\"destination\":", self.destination)
        print("\"origin\":", self.origin)
        print("\"total_price\":", self.total_price)
        print("\"travel_time\":", self.travel_time)
        print("--------------------------------")
    # def check(self, ):
    #     # is it possible
    #
    #     # check time min 1 max 6
    #
    #     # add time travel
    #
    #     # add price
    #
    #     # set current location
    #
    #     # set current time

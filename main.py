import csv
from Result import Result
from Flight import Flight
import argparse
from datetime import timedelta


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_set', type=str)
    parser.add_argument('origin', type=str)
    parser.add_argument('destination', type=str)
    parser.add_argument('--bags', type=int, default=0)
    parser.add_argument('--return', action='store_true')

    return vars(parser.parse_args())


def read_file(file_name):
    file = open(args['data_set'])
    csvreader = csv.reader(file)
    next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()
    result = []
    for elem in rows:
        result.append(Flight(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7]))
    return result


def get_possible_flights(flights: [Flight], result: Result):
    r = []

    for fl in flights:
        if fl.origin == result.current_location:
            if fl.origin not in result.visited:
                if fl.bags_allowed >= result.bags_count:
                    if result.current_time != 0:
                        if result.current_time + timedelta(hours=1) <= fl.departure <= result.current_time + timedelta(hours=6):
                            r.append(fl)
                    else:
                        r.append(fl)

    return r


def algo(trips: [Result], res: Result, flights: [Flight]):
    if res.current_location == res.destination:
        trips.append(res)
        return

    for elem in get_possible_flights(flights, res):
        a = Result()
        a.copy(res)
        a.add_flight(elem)
        algo(trips, a, flights)


if __name__ == '__main__':
    args = get_args()

    result = Result(args['origin'], args['destination'], args['bags'])
    flights = read_file(args['data_set'])

    trips = []

    algo(trips, result, flights)



    for t in trips:
        t.print()

    print(len(trips))


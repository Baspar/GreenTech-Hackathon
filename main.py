#!/usr/bin/env python3
import csv

def get_route():
    route = []
    with open('route_data.csv', 'r') as route_data:
        reader = csv.reader(route_data, delimiter=',')
        reader.__next__() # Skip headers
        for (distance_left, has_control_stop, max_speed, height_change, angle) in reader:
            route.append({
                'distance_left': int(distance_left.strip()),
                'has_control_stop': has_control_stop.strip() == "1",
                'max_speed': int(max_speed.strip()),
                'height_change': float(height_change.strip()),
                'angle': float(angle.strip()),
            })
    return route

def main():
    route = get_route()
    print(route[0])
    print(len(route))

if __name__ == "__main__":
    main()

import csv
import numpy

class Model:
    def _read_route(_self, route_file):
        route = []
        with open(route_file, 'r') as route_data:
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

    def _read_sun(_self, sun_file):
        return numpy.loadtxt(sun_file, delimiter=',')

    def _read_wind(_self, wind_file):
        return numpy.loadtxt(wind_file, delimiter=',')

    def get_route_at_km(self, km):
        rounded_km = int(km)
        return self.route[rounded_km]

    def __init__(self, route_file='route_data.csv', wind_file='interpolated_data/wndgust10m_interp.csv', sun_file='interpolated_data/av_swsfcdown_interp.csv'):
        self.route = self._read_route(route_file)
        self.wind = self._read_wind(wind_file)
        self.sun = self._read_sun(sun_file)

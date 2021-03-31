import csv

class Model:
    def _get_route(_self, route_file):
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

    def _get_sun(_self, sun_file):
        sun = []
        with open(sun_file, 'r') as file:
            for row in  csv.reader(file, delimiter=','):
                sun.append(float(value.strip()) for value in row)
        return sun

    def _get_wind(_self, wind_file):
        sun = []
        with open(wind_file, 'r') as file:
            for row in csv.reader(file, delimiter=','):
                sun.append(float(value.strip()) for value in row)
        return sun

    def __init__(self, route_file='route_data.csv', wind_file='interpolated_data/wndgust10m_interp.csv', sun_file='interpolated_data/av_swsfcdown_interp.csv'):
        self.route = self._get_route(route_file)
        self.wind = self._get_wind(wind_file)
        self.sun = self._get_sun(sun_file)

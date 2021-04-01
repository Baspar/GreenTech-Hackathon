import csv
import numpy
from datetime import datetime

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

    def _read_datetime(_self, date_file, time_file):
        with open(date_file, 'r') as date, open(time_file, 'r') as time:
            date_str = date.readline().strip()
            year, month, day = date_str[:4], date_str[4:6], date_str[6:8]
            hour = time.readline().strip()
            iso_datetime = "{}-{}-{}Z{:0>2}:00:00".format(year, month, day, hour)
            gmt_datetime = datetime.fromisoformat(iso_datetime).replace(tzinfo=pytz.timezone('Australia/Darwin'))
            return gmt_datetime

    def distance_to_index(_self, distance):
        return int(distance)

    def datetime_to_index(self, time):
        return int((time - self.start_datetime).total_seconds() / 60 / 15)

    def __init__(self,
            route_file='route_data.csv',
            wind_file='interpolated_data/wndgust10m_interp.csv',
            sun_file='interpolated_data/av_swsfcdown_interp.csv',
            date_file='interpolated_data/base_date_interp.csv',
            time_file='interpolated_data/base_time_interp.csv'):
        self.route = self._read_route(route_file)
        self.wind = self._read_wind(wind_file)
        self.sun = self._read_sun(sun_file)
        self.start_datetime = self._read_datetime(date_file, time_file)

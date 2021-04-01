import csv
import pathlib
import numpy
from datetime import datetime
import pytz

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
            gmt_datetime = datetime.fromisoformat(iso_datetime)
            offset = pytz.timezone("Australia/darwin").utcoffset(datetime.now())
            return gmt_datetime + offset

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
        root_path = pathlib.Path(__file__).parent.parent
        self.route = self._read_route("{}/{}".format(root_path, route_file))
        self.wind = self._read_wind("{}/{}".format(root_path, wind_file))
        self.sun = self._read_sun("{}/{}".format(root_path, sun_file))
        self.start_datetime = self._read_datetime("{}/{}".format(root_path, date_file), "{}/{}".format(root_path, time_file))

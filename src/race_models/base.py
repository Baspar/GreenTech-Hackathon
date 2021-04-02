from math import pi, cos, sin
from datetime import timedelta
import numpy
from logger import logger

class BaseModel:
    def __init__(self, model):
        self.model = model
        self.current_time = model.start_datetime
        self.current_km = 0.0
        self.current_battery = 5000.0
        print("\n\nStarting. Battery={}, current_distance={}, current_time={}".format(self.current_battery, self.current_km, self.current_time))

    def get_current_route_segment(self):
        route_segment_index = self.model.distance_to_index(self.current_km)
        return self.model.route[route_segment_index]

    def get_current_sun(self):
        return self.model.sun[
                self.model.distance_to_index(self.current_km),
                self.model.datetime_to_index(self.current_time)
                ]

    def get_current_wind(self):
        return self.model.wind[
                self.model.distance_to_index(self.current_km),
                self.model.datetime_to_index(self.current_time)
                ]

    def _get_production_for(self, speed, distance, time):
        return 3.6 * self.get_current_sun() * time * 0.8

    def _get_ext_forces(self, speed, distance, time):
        route_segment = self.get_current_route_segment()

        (zonal_wind, meridional_wind) = self.get_current_wind()
        theta = -2 * pi * route_segment['angle'] / 360
        rot_matrix = numpy.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
        wind_projection = numpy.dot(rot_matrix, [zonal_wind, meridional_wind])[0]
        f_drag = 0.1 * 1.1644 * (wind_projection - speed * 5 / 18) ** 2 / 2

        f_rolling = 250 * 9.81 * 0.01

        f_grav = 250 * 9.81 * route_segment['height_change'] / 1000

        return (f_drag, f_rolling, f_grav)

    def _check_for_end(self):
        if self.model.datetime_to_index(self.current_time) >= len(self.model.sun[0]):
            print("Err: no more weather data")
            return True

        if self.model.distance_to_index(self.current_km) >= len(self.model.route):
            print("Race over")
            return True

        if self.current_battery <= 0:
            print('Battery is empty')
            return True

        return False


    def rest_until(self, time):
        from_index = self.model.datetime_to_index(self.current_time)
        to_index = self.model.datetime_to_index(time)
        sun_at_this_location = self.model.sun[self.model.distance_to_index(self.current_km)]
        total_sun = 3.6 * sun_at_this_location[from_index:to_index].sum() * 0.25 * 0.8
        self.current_battery += total_sun
        self.current_battery = min(5000.0, self.current_battery)
        self.current_time = time

        logger('rest', self.current_time, 0, 0, self.current_battery, total_sun, total_sun, (0, 0, 0), self.current_km)

        if self._check_for_end():
            return True

        if not 8 <= self.current_time.hour < 17:
            current_time = self.current_time
            tommorow_morning = (current_time + timedelta(days=1)).replace(hour=8, minute=0, second=0, microsecond=0)
            return self.rest_until(tommorow_morning)

    def move(self, speed):
        minutes_to_next_km = (int(self.current_km + 1) - self.current_km) / speed * 60
        current_quarter = (self.current_time - self.model.start_datetime).total_seconds() / 60 / 15
        minutes_to_next_quarter = (int(current_quarter + 1) - current_quarter) * 15

        time = min(minutes_to_next_km, minutes_to_next_quarter) / 60
        distance = time * speed

        (f_drag, f_rolling, f_grav) = self._get_ext_forces(speed, distance, time)
        consumption = (f_drag + f_rolling + f_grav) * distance / 0.95
        production = self._get_production_for(speed, distance, time)
        delta = (production - consumption)

        self.current_battery = min(5000.0, self.current_battery + delta)
        self.current_km += distance
        self.current_time += timedelta(hours=time)


        logger('move', self.current_time, distance, speed, self.current_battery, delta, production, (f_drag, f_rolling, f_grav), self.current_km)

        if self._check_for_end():
            return True

        if not 8 <= self.current_time.hour < 17:
            current_time = self.current_time
            tommorow_morning = (current_time + timedelta(days=1)).replace(hour=8, minute=0, second=0, microsecond=0)
            return self.rest_until(tommorow_morning)
        elif self.get_current_route_segment()['has_control_stop']:
            return self.rest_until(self.current_time + timedelta(minutes=30))

    def step(self):
        raise Exception("Please reimplement this step method")

from datetime import timedelta

class BaseModel:
    def __init__(self, model):
        self.model = model
        self.current_time = model.start_datetime
        self.current_km = 0.0
        self.current_battery = 5000.0

    def _get_production_for(self, speed, distance, time):
        return 0

    def _get_consumption_for(self, speed, distance, time):
        return 200

    def move(self, speed):
        minutes_to_next_km = (int(self.current_km + 1) - self.current_km) / speed * 60
        current_quarter = (self.current_time - self.model.start_datetime).total_seconds() / 60 / 15
        minutes_to_next_quarter = (int(current_quarter + 1) - current_quarter) * 15

        time = min(minutes_to_next_km, minutes_to_next_quarter) / 60
        distance = time * speed

        consumption = self._get_consumption_for(speed, distance, time)
        production = self._get_production_for(speed, distance, time)

        self.current_battery += (production - consumption)
        self.current_km += distance
        self.current_time += timedelta(hours=time)

        print("Moving {}km, at {}km/h. Battery={}, current_distance={}, current_time={}".format(distance, speed, self.current_battery, self.current_km, self.current_time))

    def get_current_route_segment(self):
        route_segment_index = self.model.distance_to_index(self.current_km)
        return self.model.route[route_segment_index]

    def step(self):
        raise Exception("Please reimplement this step method")

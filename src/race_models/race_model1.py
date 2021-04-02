from datetime import timedelta
from .base import BaseModel

class RaceModel1(BaseModel):
    def step(self):
        current_route_segment = self.get_current_route_segment()
        self.move(min(32, current_route_segment['max_speed']))
        if self.model.datetime_to_index(self.current_time) >= len(self.model.sun[0]):
            print("Err: no more weather data")
            return False
        return True

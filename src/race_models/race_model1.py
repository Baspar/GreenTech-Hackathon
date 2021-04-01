from datetime import timedelta
from .base import BaseModel

class RaceModel1(BaseModel):
    def step(self):
        current_route_segment = self.get_current_route_segment()
        self.move(min(30, current_route_segment['max_speed']))

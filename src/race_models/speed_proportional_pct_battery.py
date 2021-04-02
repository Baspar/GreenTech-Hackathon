from datetime import timedelta
from .base import BaseModel

class Model(BaseModel):
    def step(self):
        current_route_segment = self.get_current_route_segment()
        max_speed = min(100, current_route_segment['max_speed'])
        percentage_bat = self.current_battery / 5000.0
        return self.move(percentage_bat * max_speed)

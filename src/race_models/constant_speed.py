from datetime import timedelta
from .base import BaseModel

def Model(speed):
    class Model(BaseModel):
        def step(self):
            current_route_segment = self.get_current_route_segment()
            max_speed = current_route_segment['max_speed']
            return self.move(min(speed, max_speed))
    return Model

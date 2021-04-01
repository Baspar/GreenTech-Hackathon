from datetime import timedelta
from .base import BaseModel

class RaceModel1(BaseModel):
    def step(self):
        route_segment = self.get_current_route_segment()
        if 8 <= self.current_time.hour < 17:
            self.move(20)
        else:
            current_time = self.current_time
            tommorow_morning = (current_time + timedelta(days=1)).replace(hour=8, minute=0, second=0, microsecond=0)
            self.rest_until(tommorow_morning)

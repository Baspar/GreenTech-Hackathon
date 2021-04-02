import math
from datetime import timedelta
from .base import BaseModel

class Model(BaseModel):
    use_bat_percentage = None

    def step(self):
        if self.current_battery < 0:
            tommorow_morning = (self.current_time + timedelta(days=1)).replace(hour=8, minute=0, second=0, microsecond=0)
            self.rest_until(tommorow_morning)

        current_route_segment = self.get_current_route_segment()

        max_speed = min(120, current_route_segment['max_speed'])

        percentage_bat = self.current_battery / 5000.0

        return self.move(min(max_speed, percentage_bat * max_speed))

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

        is_afternoon = self.current_time.hour >= 16
        is_almost_over = (3027 - self.current_km) < 60

        if is_afternoon or is_almost_over:
            return self.move(percentage_bat ** 0.2 * max_speed)
        else:
            return self.move(min(max_speed, percentage_bat * max_speed))

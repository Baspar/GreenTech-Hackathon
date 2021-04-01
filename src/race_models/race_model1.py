from .base import BaseModel

class RaceModel1(BaseModel):
    def step(self):
        route_segment = self.get_current_route_segment()
        self.move(route_segment['max_speed'])

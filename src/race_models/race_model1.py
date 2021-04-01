from .base import BaseModel

class RaceModel1(BaseModel):
    def step(self):
        route_segment_index = self.model.distance_to_index(self.current_km)
        route_segment = self.model.route[route_segment_index]
        max_speed = route_segment['max_speed']
        self.move(max_speed)

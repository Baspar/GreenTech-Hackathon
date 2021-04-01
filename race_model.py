class RaceModel:
    def __init__(self, model):
        self.model = model
        self.current_time = 0.0
        self.current_km = 0.0
        self.current_battery = 5000.0

    def move(self, km=0, time=0, speed):
        if km == 0:
            km = time * speed

    def rest(self, time):
        return

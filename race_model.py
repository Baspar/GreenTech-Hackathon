class RaceModel:
    def __init__(self, model):
        self.model = model
        self.current_time = model.start_datetime
        self.current_km = 0.0
        self.current_battery = 5000.0

    def move(self, speed, distance=None, time=None):
        if distance == None and time == None:
            raise Exception('Specify a distance or a time')

        distance = distance if distance != None else time * speed
        time = time if time != None else distance / speed

    def rest(self, time):
        return

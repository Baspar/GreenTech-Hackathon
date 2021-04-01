#!/usr/bin/env python3
from model import Model
from race_models.race_model1 import RaceModel1

def main():
    model = Model()
    race = RaceModel1(model)
    while race.current_km < len(model.route):
        race.step()
        if race.current_battery <= 0:
            print('Battery is empty')
            return

if __name__ == "__main__":
    main()

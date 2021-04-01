#!/usr/bin/env python3
from model import Model
from race_model import RaceModel

def main():
    model = Model()
    race = RaceModel(model)
    print(model.get_route_at_km(.5))

if __name__ == "__main__":
    main()

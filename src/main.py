#!/usr/bin/env python3
from model import Model
import race_models

def main():
    model = Model()
    race = race_models.get('proportional')(model)

    while race.current_km < len(model.route):
        race_ended = race.step()
        if race_ended:
            return

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import sys
from datetime import datetime
from model import Model
import race_models

def main():
    model = Model()
    if len(sys.argv) < 2:
        print("Provide model name")
        return 0

    model_name = sys.argv[1]
    race = race_models.get(model_name)(model)

    while race.current_km < len(model.route):
        race_ended = race.step()
        if race_ended:
            return

if __name__ == "__main__":
    main()

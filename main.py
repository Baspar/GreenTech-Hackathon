#!/usr/bin/env python3
from model import Model

def main():
    model = Model()
    print(model.get_route_at_km(.5))

if __name__ == "__main__":
    main()

from . import constant_speed, battery, battery_sun_sprint

def get(model):
    if model == 'constant':
        return constant_speed.Model
    elif model == 'battery':
        return battery.Model
    elif model == 'battery_sun_sprint':
        return battery_sun_sprint.Model
    else:
        raise Exception('Model "{}" not found'.format(model))

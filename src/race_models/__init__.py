from . import constant_speed, battery_sprint, battery, battery_sun_sprint

def get(model):
    if model == 'constant':
        return constant_speed.Model(30)
    elif model == 'battery':
        return battery.Model
    elif model == 'battery_sprint':
        return battery_sprint.Model
    elif model == 'battery_sun_sprint':
        return battery_sun_sprint.Model
    else:
        raise Exception('Model "{}" not found'.format(model))

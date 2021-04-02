from . import constant_speed, speed_proportional_pct_battery

def get(model):
    if model == 'constant':
        return constant_speed.Model
    elif model == 'proportional':
        return speed_proportional_pct_battery.Model
    else:
        raise Exception('Model "{}" not found'.format(model))

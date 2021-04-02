CSV = False
headers = False

def logger(action, datetime, distance_moved, speed, battery, delta, solar_production, ext_force, total_distance):
    (f_drag, f_rolling, f_grav) = ext_force
    # if not headers:
    #     headers = True
    #     print('action, datetime, distance_moved, speed, battery, delta_battery, solar_production, f_drag, f_rolling, f_grav, current_km')

    if CSV:
        print('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(action, datetime, distance_moved, speed, battery, delta, solar_production, f_drag, f_rolling, f_grav, total_distance))
    elif action == 'move':
        print("Moving {:.4f}km, at {:.4f}km/h. Battery={:.4f} (Δ{: .4f}), current_distance={:.4f}, current_time={}".format(distance_moved, speed, battery, delta, total_distance, datetime))
    elif action == 'rest':
        print("Resting until {}. Battery={:.4f} (Δ{: .4f}), current_distance={:.4f}\n\n".format(datetime, battery, delta, total_distance))

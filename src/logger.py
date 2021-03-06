CSV = False

def logger(action, datetime, distance_moved, speed, battery, delta, solar_production, ext_force, total_distance, start_datetime):
    (f_drag, f_rolling, f_grav) = ext_force

    if CSV:
        print('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(action, (datetime - start_datetime).total_seconds(), distance_moved, speed, battery, delta, solar_production, f_drag, f_rolling, f_grav, total_distance))
    elif action == 'move':
        print("Moving {:.4f}km, at {:.4f}km/h. Battery={:.4f} (Δ{: .4f}), current_distance={:.4f}, current_time={}".format(distance_moved, speed, battery, delta, total_distance, datetime))
    elif action == 'rest':
        print("Resting until {}. Battery={:.4f} (Δ{: .4f}), current_distance={:.4f}\n\n".format(datetime, battery, delta, total_distance))

from geopy.distance import geodesic


def calculate_distance(car, cargo) -> float:
    car_location = (car.current_location.latitude, car.current_location.longitude)
    cargo_location = (cargo.pick_up_location.latitude, cargo.pick_up_location.longitude)
    return geodesic(car_location, cargo_location).miles

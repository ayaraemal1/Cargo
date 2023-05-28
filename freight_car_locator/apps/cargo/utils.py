from geopy.distance import geodesic


def calculate_distance(car, cargo) -> float:
    """
    Calculate the distance in miles between the current location of a car and the pick-up location of a cargo.

    Args:
        car: The Car instance representing the car.
        cargo: The Cargo instance representing the cargo.

    Returns:
        The distance in miles between the car's current location and the cargo's pick-up location.
    """
    car_location = (car.current_location.latitude, car.current_location.longitude)
    cargo_location = (cargo.pick_up_location.latitude, cargo.pick_up_location.longitude)
    return geodesic(car_location, cargo_location).miles

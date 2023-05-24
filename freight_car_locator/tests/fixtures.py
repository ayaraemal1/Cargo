import pytest

from apps.cargo.models import Cargo
from random import randint


@pytest.fixture
def cargo_data(db):
    random_location_ids = (
        (10, 15),
        (20, 25),
        (30, 35),
        (40, 45),
        (50, 55),
        (60, 65),
        (70, 75),
        (80, 85),
        (90, 95),
        (100, 150),
    )
    for i in range(0, len(random_location_ids)):
        Cargo.objects.create(
            pick_up_location_id=random_location_ids[i][0],
            delivery_location_id=random_location_ids[i][1],
            weight=randint(1, 1000),
            description=f"Cargo {i}",
        )

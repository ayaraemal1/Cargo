import pytest

from apps.cargo.models import Cargo
from random import randint

from apps.location.models import Location

CARGOES_NUMBER = 10


@pytest.fixture
def cargo_data(db):
    locations_count = Location.objects.count()
    locations_list = Location.objects.all()
    cargoes = []
    for i in range(CARGOES_NUMBER):
        random_index_1 = randint(0, locations_count - 1)
        random_index_2 = randint(0, locations_count - 1)
        cargoes.append(
            Cargo(
                pick_up_location=locations_list[random_index_1],
                delivery_location=locations_list[random_index_2],
                weight=randint(1, 1000),
                description=f"Cargo {i}",
            )
        )
    Cargo.objects.bulk_create(cargoes)

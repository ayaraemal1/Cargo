from decimal import Decimal

from rest_framework import status
from rest_framework.reverse import reverse

from apps.cargo.models import Cargo
from tests.fixtures import cargo_data

CARGO_DATA = {
    "pick_up_location_zip": 74130,
    "delivery_location_zip": 71999,
    "weight": Decimal(12.4),
    "description": "parcel",
}

CARGO_UPDATE_DATA = {"weight": Decimal(150.47), "description": "parcel_updated"}

FILTERS_DATA = {
    "weight_from": 10,
    "weight_to": 50,
    "nearest_cars_miles": 1000,
}


def test_create_data(client, db):
    """Tests the data returned by the cargo-create endpoint."""
    response = client.post(reverse("cargoes:cargo-list"), data=CARGO_DATA)
    record_id = response.json()["id"]
    record = Cargo.objects.get(id=record_id)
    assert all(item in record.__dict__.items() for item in CARGO_DATA.items())


def test_list_data(client, cargo_data):
    """Tests the data returned by the cargo-list endpoint."""
    response = client.get(reverse("cargoes:cargo-list"), data=FILTERS_DATA)
    response_data = response.json()
    assert type(response_data) == list
    for item in response_data:
        assert item.keys() == ("pick_up_location", "delivery_location", "nearest_cars_number")


def test_retrieve_data(client, cargo_data):
    """Tests the data returned by the cargo-retrieve endpoint."""
    response = client.post(reverse("cargoes:cargo-detail", args=[1]))
    response_data = response.json()
    assert response_data.keys() == ("pick_up_location", "delivery_location", "weight", "description", "nearest_cars")
    assert type(response_data["nearest_cars"]) == list


def test_update_data(client, cargo_data):
    """Tests the data returned by the cargo-retrieve endpoint."""
    response = client.patch(reverse("cargoes:cargo-detail", args=[5]), data=CARGO_UPDATE_DATA)
    assert response.json()["description"] == CARGO_UPDATE_DATA["description"]


def test_delete_data(client, cargo_data):
    """Tests the data returned by the cargo-retrieve endpoint."""
    initial_count = Cargo.objects.count()
    response = client.delete(reverse("cargoes:cargo-detail", args=[5]))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Cargo.objects.count() == initial_count - 1

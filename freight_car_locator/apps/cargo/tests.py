from decimal import Decimal

from rest_framework import status
from rest_framework.reverse import reverse

from apps.cargo.models import Cargo
from tests.fixtures import cargo_data

CARGO_DATA = {
    "pick_up_location": "74130",
    "delivery_location": "71999",
    "weight": "12.4",
    "description": "parcel",
}

CARGO_UPDATE_DATA = {"weight": "150.47", "description": "parcel_updated"}

FILTERS_DATA = {
    "weight_from": 10,
    "weight_to": 50,
    "cars_max_distance": 1000,
}


def test_create_data(client, db):
    """Tests the data returned by the cargo-create endpoint."""
    response = client.post(reverse("cargoes:cargo-list"), data=CARGO_DATA)
    record_id = response.json()["id"]
    record = Cargo.objects.get(id=record_id)
    assert CARGO_DATA["pick_up_location"] == response.json()["pick_up_location"]
    assert CARGO_DATA["pick_up_location"] == record.pick_up_location.pk


def test_list_data(client, cargo_data):
    """Tests the data returned by the cargo-list endpoint."""
    response = client.get(reverse("cargoes:cargo-list"), data=FILTERS_DATA)
    response_data = response.json()
    assert type(response_data) == list
    for item in response_data:
        assert tuple(item.keys()) == ("id", "pick_up_location", "delivery_location", "nearest_cars_number")


def test_retrieve_data(client, cargo_data):
    """Tests the data returned by the cargo-retrieve endpoint."""
    idx = Cargo.objects.first().id
    response = client.get(reverse("cargoes:cargo-detail", args=[idx]))
    response_data = response.json()
    assert tuple(response_data.keys()) == (
        "id",
        "pick_up_location",
        "delivery_location",
        "weight",
        "description",
        "cars",
    )
    assert type(response_data["cars"]) == list


def test_update_data(client, cargo_data):
    """Tests the data returned by the cargo-retrieve endpoint."""
    idx = Cargo.objects.first().id
    response = client.patch(
        reverse("cargoes:cargo-detail", args=[idx]), data=CARGO_UPDATE_DATA, content_type="application/json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["description"] == CARGO_UPDATE_DATA["description"]


def test_delete_data(client, cargo_data):
    """Tests the data returned by the cargo-retrieve endpoint."""
    initial_count = Cargo.objects.count()
    idx = Cargo.objects.first().id
    response = client.delete(reverse("cargoes:cargo-detail", args=[idx]))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Cargo.objects.count() == initial_count - 1

import pytest
from rest_framework import status
from rest_framework.reverse import reverse

UPDATE_LOCATION_DATA = {"current_location": "74130"}


def test_update_status_code(client, db):
    """Tests the status code of the car-update endpoint."""
    response = client.patch(
        reverse("cars:car-detail", args=[1]), data=UPDATE_LOCATION_DATA, content_type="application/json"
    )
    assert response.status_code == status.HTTP_200_OK


def test_update_data(client, db):
    """Tests the data returned by the car-update endpoint."""
    response = client.patch(
        reverse("cars:car-detail", args=[1]), data=UPDATE_LOCATION_DATA, content_type="application/json"
    )
    assert response.json() == UPDATE_LOCATION_DATA

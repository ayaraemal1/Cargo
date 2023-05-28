from django.db import models


class Location(models.Model):
    """
    A class representing a location.

    Attributes:
        city (str): The city of the location.
        state (str): The state of the location.
        zip_code (str): The postal code of the location (primary key).
        latitude (float): The latitude coordinate of the location.
        longitude (float): The longitude coordinate of the location.
        created (datetime): The datetime when the location was created.
        updated (datetime): The datetime when the location was last updated.
    """

    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=12, primary_key=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.city} ({self.latitude}, {self.longitude})"

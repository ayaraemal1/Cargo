from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models

from apps.location.models import Location


class Car(models.Model):
    """
    A class representing a car.

    Attributes:
        unique_number (str): The unique number of the car in the format "1234A", "2534B", etc.
        current_location (Location): The current location of the car.
        load_capacity (Decimal): The load capacity of the car.
        created (datetime): The datetime when the car data was created.
        updated (datetime): The datetime when the car data was last updated.
    """

    unique_number = models.CharField(
        max_length=5,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[1-9][0-9]{3}[A-Z]$",
                message="Number must be in the format of number from 1000 to 9999 + random uppercase letter from the English alphabet at the end.",
            )
        ],
    )
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    load_capacity = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(1, message="Weight must be at least 1.0."),
            MaxValueValidator(1000, message="Weight cannot exceed 1000.0."),
        ],
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unique_number

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.location.models import Location


class Cargo(models.Model):
    """Stores cargo information"""

    pick_up_location = models.ForeignKey(Location, related_name="pick_up_cargos", on_delete=models.CASCADE)
    delivery_location = models.ForeignKey(Location, related_name="delivery_cargos", on_delete=models.CASCADE)
    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(1, message="Weight must be at least 1.0."),
            MaxValueValidator(1000, message="Weight cannot exceed 1000.0."),
        ],
        db_index=True,
    )
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cargo ID: {self.pk}"

from rest_framework.serializers import ModelSerializer, ReadOnlyField, SerializerMethodField

from .models import Cargo
from .utils import calculate_distance
from ..car.models import Car


class CargoCreateSerializer(ModelSerializer):
    """
    A serializer class for creating Cargo instances.
    Serializes all the fields of a Cargo instance, except 'created' and 'updated'.
    """

    id = ReadOnlyField()

    class Meta:
        model = Cargo
        exclude = ("created", "updated")


class CargoEditSerializer(ModelSerializer):
    """
    A serializer class for editing Cargo instances.

    Serializes the weight and description fields of a Cargo instance.
    """

    class Meta:
        model = Cargo
        fields = ("weight", "description")


class CarDistanceSerializer(ModelSerializer):
    """
    A serializer class for calculating the distance between a Car instance and a Cargo instance.
    Serializes the unique_number and calculated distance fields of a Car instance.
    """

    distance = SerializerMethodField()

    def get_distance(self, obj):
        cargo = self.context["cargo"]
        distance = calculate_distance(obj, cargo)
        return distance

    class Meta:
        model = Car
        fields = ["unique_number", "distance"]


class CargoDetailSerializer(ModelSerializer):
    """
    A serializer class for detailed representation of Cargo instances.

    Serializes the id, pick_up_location, delivery_location, weight, description fields
    of a Cargo instance and cars using CarDistanceSerializer.
    """

    cars = SerializerMethodField()

    @staticmethod
    def get_cars(obj: Cargo) -> list:
        """
        Retrieves the list of cars sorted by distance from the Cargo instance.

        Args:
            obj: The Cargo instance.

        Returns:
            The sorted by distance list of cars.
        """
        cars = Car.objects.select_related("current_location").all()
        serializer = CarDistanceSerializer(cars, many=True, context={"cargo": obj})
        return sorted(serializer.data, key=lambda car: car["distance"])

    class Meta:
        model = Cargo
        fields = ["id", "pick_up_location", "delivery_location", "weight", "description", "cars"]


class CargoListSerializer(ModelSerializer):
    """
    A serializer class for listing Cargo instances.
    Serializes the id, pick_up_location, delivery_location fields of a Cargo instance and number of the nearest cars.
    """

    nearest_cars_number = SerializerMethodField()

    def get_nearest_cars_number(self, obj: Cargo) -> int:
        """
        Calculates the number of nearest cars to the Cargo instance.

        Args:
            obj: The Cargo instance.

        Returns:
            The number of nearest cars.
        """
        max_distance = self.context.get("cars_max_distance")

        cars = Car.objects.select_related("current_location").all()
        n = 0
        for car in cars:
            distance = calculate_distance(car, obj)
            if distance <= max_distance:
                n += 1
        return n

    class Meta:
        model = Cargo
        fields = ("id", "pick_up_location", "delivery_location", "nearest_cars_number")

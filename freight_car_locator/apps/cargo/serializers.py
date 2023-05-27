from rest_framework.serializers import ModelSerializer, ReadOnlyField, SerializerMethodField

from .models import Cargo
from .utils import calculate_distance
from ..car.models import Car


class CargoCreateSerializer(ModelSerializer):
    id = ReadOnlyField()

    class Meta:
        model = Cargo
        exclude = ("created", "updated")


class CargoEditSerializer(ModelSerializer):
    class Meta:
        model = Cargo
        fields = ("weight", "description")


class CarDistanceSerializer(ModelSerializer):
    distance = SerializerMethodField()

    def get_distance(self, obj):
        cargo = self.context["cargo"]
        distance = calculate_distance(obj, cargo)
        return distance

    class Meta:
        model = Car
        fields = ["unique_number", "distance"]


class CargoDetailSerializer(ModelSerializer):
    cars = SerializerMethodField()

    @staticmethod
    def get_cars(obj):
        cars = Car.objects.select_related("current_location").all()
        serializer = CarDistanceSerializer(cars, many=True, context={"cargo": obj})
        return sorted(serializer.data, key=lambda car: car["distance"])

    class Meta:
        model = Cargo
        fields = ["id", "pick_up_location", "delivery_location", "weight", "description", "cars"]


class CargoListSerializer(ModelSerializer):
    nearest_cars_number = SerializerMethodField()

    def get_nearest_cars_number(self, obj):
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

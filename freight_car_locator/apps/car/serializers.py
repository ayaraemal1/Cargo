from rest_framework.serializers import ModelSerializer, CharField

from apps.car.models import Car


class CarSerializer(ModelSerializer):
    """
    A serializer class for the Car model.
    Serializes the current_location field of a Car instance.
    """

    class Meta:
        model = Car
        fields = ("current_location",)

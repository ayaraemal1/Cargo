from rest_framework.serializers import ModelSerializer, CharField

from apps.car.models import Car


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ("current_location",)

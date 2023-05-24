from rest_framework.serializers import ModelSerializer, CharField

from apps.car.models import Car


class CarSerializer(ModelSerializer):
    current_location_zip = CharField()

    class Meta:
        model = Car
        fields = ("current_location_zip",)

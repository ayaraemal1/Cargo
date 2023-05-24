from rest_framework.serializers import ModelSerializer

from .models import Cargo


class CargoSerializer(ModelSerializer):
    class Meta:
        model = Cargo
        exclude = ("id", "created", "updated")

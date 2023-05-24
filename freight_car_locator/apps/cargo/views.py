from rest_framework.viewsets import ModelViewSet

from .models import Cargo
from .serializers import CargoSerializer


class CargoViewSet(ModelViewSet):
    """The viewset responsible for Cargo data."""

    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

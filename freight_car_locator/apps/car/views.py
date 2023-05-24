from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Car
from .serializers import CarSerializer


class CarViewSet(GenericViewSet, UpdateModelMixin):
    """The viewset responsible for car data editing."""

    queryset = Car.objects.all()
    serializer_class = CarSerializer

from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Car
from .serializers import CarSerializer


class CarViewSet(GenericViewSet, UpdateModelMixin):
    """
    A view set for the Car model.

    Provides the ability to update a Car instance.

    Attributes:
        queryset (QuerySet): The queryset of all Car instances.
        serializer_class (CarSerializer): The serializer class to use for Car instances.
    """

    queryset = Car.objects.all()
    serializer_class = CarSerializer

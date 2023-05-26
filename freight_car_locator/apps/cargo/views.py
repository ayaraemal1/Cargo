from decimal import Decimal, InvalidOperation

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Cargo
from .serializers import CargoCreateSerializer, CargoDetailSerializer, CargoEditSerializer, CargoListSerializer


class CargoViewSet(ModelViewSet):
    """Cargo data manipulations (create, list, retrieve, update, delete methods)"""

    DEFAULT_MAX_DISTANCE = 450

    queryset = Cargo.objects.select_related("pick_up_location").all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CargoDetailSerializer
        elif self.action == "update":
            return CargoEditSerializer
        elif self.action == "list":
            return CargoListSerializer
        else:
            return CargoCreateSerializer

    def list(self, request, *args, **kwargs):
        """Adding filters to list method"""
        queryset = self.queryset
        weight_from = request.query_params.get("weight_from")
        weight_to = request.query_params.get("weight_to")
        cars_max_distance = request.query_params.get("cars_max_distance")
        try:
            if weight_from:
                queryset = queryset.filter(weight__gte=Decimal(weight_from))
            if weight_to:
                queryset = queryset.filter(weight__lte=Decimal(weight_to))
            if cars_max_distance:
                cars_max_distance = float(cars_max_distance)
            else:
                cars_max_distance = self.DEFAULT_MAX_DISTANCE
        except (InvalidOperation, ValueError):
            raise ValidationError("Filter parameter must be a number.")

        serializer = self.get_serializer(queryset, many=True, context={"cars_max_distance": cars_max_distance})
        return Response(serializer.data)

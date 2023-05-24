from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cars/", include("apps.car.urls")),
    path("api/cargoes/", include("apps.cargo.urls")),
]

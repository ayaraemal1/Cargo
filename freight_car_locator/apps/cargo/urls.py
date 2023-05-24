from rest_framework import routers

from .views import CargoViewSet

app_name = "cargoes"

router = routers.SimpleRouter()
router.register("", CargoViewSet)

urlpatterns = router.urls

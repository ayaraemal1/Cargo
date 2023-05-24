from rest_framework import routers

from .views import CarViewSet

app_name = "cars"

router = routers.SimpleRouter()
router.register("", CarViewSet)

urlpatterns = router.urls

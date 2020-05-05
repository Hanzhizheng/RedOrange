from django.urls import path
from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register('province', views.ProvinceViewSet)
router.register('city', views.CityViewSet)
router.register('area', views.AreaViewSet)


urlpatterns = router.urls
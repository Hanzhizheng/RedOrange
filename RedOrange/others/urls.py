from django.urls import path
from common import routers

from . import views


router = routers.PUTNotAllowedRouter()
router.register('province', views.ProvinceViewSet)
router.register('city', views.CityViewSet)
router.register('area', views.AreaViewSet)
router.register('city', views.JobCategoryViewSet)
router.register('area', views.JobSubCategoryViewSet)

urlpatterns = router.urls
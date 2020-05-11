from django.urls import path
from common import routers

from . import views


router = routers.PUTNotAllowedRouter()
router.register('fulltime_job', views.FullTimeJobViewSet)
router.register('parttime_job', views.PartTimeJobViewSet)
router.register('personal_job', views.PersonalJobViewSet)

urlpatterns = router.urls
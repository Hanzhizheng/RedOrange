from django.urls import path
from common import routers

from . import views

router = routers.PUTNotAllowedRouter()
router.register('user', views.UserViewSet)
router.register('job_card', views.JobCardViewSet)

urlpatterns = router.urls
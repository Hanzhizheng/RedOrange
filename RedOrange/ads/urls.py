from django.urls import path
from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register('partya', views.PartyAViewSet)
router.register('photo_album', views.PhotoAlbumViewSet)
router.register('campaign', views.CampaignViewSet)


urlpatterns = router.urls
from django.urls import path
from common import routers
from . import views


router = routers.PUTNotAllowedRouter()
router.register('partya', views.PartyAViewSet)
router.register('photo_album', views.PhotoAlbumViewSet)
router.register('campaign', views.CampaignViewSet)


urlpatterns = router.urls
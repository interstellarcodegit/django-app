from rest_framework import routers
from .api import UpdatesViewSet

router= routers.DefaultRouter()
router.register('updates', UpdatesViewSet, 'updates' )

urlpatterns= router.urls
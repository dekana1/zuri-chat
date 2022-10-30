from django.urls import include, path

from rest_framework import routers

from zuri_chat.views import BioViewSet

router = routers.DefaultRouter()
router.register(r'', BioViewSet)


urlpatterns = [
   path('', include(router.urls)),
]